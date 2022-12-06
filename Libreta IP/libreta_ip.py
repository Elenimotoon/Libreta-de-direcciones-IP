import tkinter as tk
#↑ importamos tkinter y lo llamamos tk para abreviar
# despues traemos todos lo que usamos con from e import.
from tkinter import ttk
# ↑ tambien importamos la libreria ttk que nos permite hacer tablas.
from tkinter import messagebox
# ↑ Y también la librería para hacer mensajes emergentes
from Almacenamiento.cont_bdata import *
# ↑ esta es la base de datos para guardar o importar los datos
from PIL import ImageTk, Image
# ↑ PIL es una libreria para redimencionar imagenes
from ipaddress import ip_address, IPv4Address, IPv6Address
# ↑ es para comprobar y validar la ip
#↓ estos son para crear el exel y los envia a la carpeta de documentos
import xlsxwriter
from time import sleep
import shutil 

from time import sleep
from platform import system
from subprocess import call
import re

imagen = [2]

try:
    leer_datos()
except:
    crearBD()
    crear_tabla()
# ↑ Si el archivo no existe lo creo y especifico sus funciones

def ping(host):
    parametro = '-n' if system().lower() == 'windows' else '-c' 
    comando = ['ping', parametro, '1', host] 
    devol = call(comando)
    return devol

# esta es una etiqueta que desaparece.
def lable_var(pal_var, pos_x=15, pos_y=475):
    texto = pal_var
    etiq_var = tk.Label(ventana, text=texto)
    etiq_var.place(x=pos_x, y=pos_y)
    etiq_var.config(fg=blanco,
                    bg=negro,
                    font=Tam_y_Letr)
    etiq_var.after(3000, lambda: etiq_var.destroy())
    #↑ esta linea desaparece la etiqueta

def camb_imag(imagn, tam1, tam2):
    imag_entr = Image.open(imagn)
    imag_entr = imag_entr.resize((tam1, tam2), Image.Resampling.LANCZOS)
    imag_sal = ImageTk.PhotoImage(imag_entr)
    return imag_sal

# ↓ es para que muestre si la ip es valida
def validate_ip_address(ip_string):
    try:
        ip_object = ip_address(ip_string)
        return f"la ip {ip_object} existe"
    except ValueError:
        return f"la ip {ip_string} no existe"

def ping_ipv6():
    col3 = ipv6.get() 
    validacion = validate_ip_address(col3)
    lable_var(validacion)
    sleep(3)
    devol = ping(col3)
    lable_var(devol)
    if devol == 0:
        lable_var(f'la ip {col3} esta en uso')
    elif devol != 0:
        lable_var(f'la ip {col3} no esta conectada o no esta en uso')

def ping_ipv4():
    col2 = ipv4.get()
    validacion = validate_ip_address(col2)
    lable_var(validacion)
    sleep(3)
    devol = ping(col2)
    if devol == 0:
        lable_var(f'la ip {col2} esta en uso')
    elif devol != 0:
        lable_var(f'la ip {col2} no esta conectada o no esta en uso')

def verificar_mac_address(address):
    regex = ("^([0-9A-Fa-f]{2}[:-])" +
            "{5}([0-9A-Fa-f]{2})|" +
            "([0-9a-fA-F]{4}\\." +
            "[0-9a-fA-F]{4}\\." +
            "[0-9a-fA-F]{4})$")
    verificador = re.compile(regex)
    
    if re.search(verificador, address):
        return True
    return False

def borrar_datos():
    item = tbl.item(tbl.focus())
    if len(item['values']) == 0:
        return messagebox.showerror("Error", "No se ha proporcionado un nodo a eliminar")
    if messagebox.askyesno("Advertencia", "¡Si elimina este nodo no habrá vuelta atrás!\n\n¿Está seguro?"):
        identificador = item['values'][0]
        
        eliminar_filas(identificador)
        actualizar_tabla()
        lable_var(f'{identificador} fue eliminado')

#↓ configuracion de los botones    
def guardar():
    col1 = equipos.get()
    col2 = ipv4.get()
    col3 = ipv6.get()
    col4 = mac_addr.get()
    col5 = usser.get()
    col6 = tipo_e.get()
    
    verificar = [col1, col2, col3, col4, col5, col6]
    
    if any(valor == '' for valor in verificar):
        return messagebox.showerror("Error", "No se han proporcionado los campos necesarios")
    
    try:
        IPv4Address(col2)
    except:
        return messagebox.showerror("Error", "La dirección otorgada no corresponde a una IPv4 válida")
    try:
        IPv6Address(col3)
    except:
        return messagebox.showerror("Error", "La dirección otorgada no corresponde a una IPv6 válida")
    
    if not verificar_mac_address(col4):
        return messagebox.showerror("Error", "La dirección otorgada no corresponde a una Mac Address válida")
    
    for equipo in leer_datos():
        if list(equipo) == verificar:
            return messagebox.showerror("Error", "¡El equipo ya existe!")
        elif col1 == equipo[0]:
            return messagebox.showerror("Error", "¡No se pueden nombrar dos equipos con el mismo valor!")
    
    ins_datos(col1, col2, col3, col4, col5, col6)
    actualizar_tabla()
    
    col1 = equipos.set("")
    col2 = ipv4.set("")
    col3 = ipv6.set("")
    col4 = mac_addr.set("")
    col5 = usser.set("")
    col6 = tipo_e.set("")
    lable_var('Datos guardados')

#↓ Esto "sube" la información de las columnas hacia las cajas
def subir_columna(evento):
    item = tbl.item(tbl.focus())
    equipos.set(item['values'][0])
    ipv4.set(item['values'][1])
    ipv6.set(item['values'][2])
    mac_addr.set(item['values'][3])
    usser.set(item['values'][4])
    tipo_e.set(item['values'][5])

#↓ esto guarda los elementos en la lista de ventana.
def actualizar_tabla():
    tbl.delete(*tbl.get_children())
    
    lista_cruda = leer_datos()
    
    for columnas in lista_cruda:
        tbl.insert("", 'end', values=columnas)

def edit_datos():
    item = tbl.item(tbl.focus())
    if len(item['values']) == 0:
        return messagebox.showerror("Error", "No se ha proporcionado un nodo a actualizar")
    identificador = item['values'][0]
    
    col1 = equipos.get()
    col2 = ipv4.get()
    col3 = ipv6.get() 
    col4 = mac_addr.get() 
    col5 = usser.get() 
    col6 = tipo_e.get()
    
    verificar = [col1, col2, col3, col4, col5, col6]
    
    if any(valor == '' for valor in verificar):
        return messagebox.showerror("Error", "No se han proporcionado los campos necesarios")
    
    try:
        IPv4Address(col2)
    except:
        return messagebox.showerror("Error", "La dirección otorgada no corresponde a una IPv4 válida")
    try:
        IPv6Address(col3)
    except:
        return messagebox.showerror("Error", "La dirección otorgada no corresponde a una IPv6 válida")
    
    if not verificar_mac_address(col4):
        return messagebox.showerror("Error", "La dirección otorgada no corresponde a una Mac Address válida")
    
    for equipo in leer_datos():
        if not identificador == col1 and col1 == equipo[0]:
            return messagebox.showerror("Error", "¡No se pueden nombrar dos equipos con el mismo valor!")
    
    if item['values'] == verificar:
        return messagebox.showerror("Error", "¡No hay cambios que modificar!")
    
    if messagebox.askyesno("Advertencia", f"¡Está apunto de cambiar los valores de {identificador}!\n\n¿Está seguro de hacerlo?"):
        editar_datos(col1, col2, col3, col4, col5, col6, identificador)
        actualizar_tabla()
        
        col1 = equipos.set("")
        col2 = ipv4.set("")
        col3 = ipv6.set("")
        col4 = mac_addr.set("")
        col5 = usser.set("")
        col6 = tipo_e.set("") 
        lable_var('Datos editados')

def cambiar_fondo(direccion):
    posicion = imagen[0] + direccion
    
    if posicion >= len(fond_vent):
        imagen.pop()
        imagen.append(0)
    elif posicion < 0:
        imagen.pop()
        imagen.append(len(fond_vent)-1)
    else:
        imagen.pop()
        imagen.append(posicion)
    
    fondo_ventana.config(image=fond_vent[imagen[0]])
    fondo_ventana.pack()
    


def Crear_excel () :
    lista_cruda = leer_datos()
    archivo=xlsxwriter.Workbook('directorio-ip.xlsx')
    hoja=archivo.add_worksheet()
    for i in range(len(lista_cruda)):
        fila = list (lista_cruda[i])
        for c in range(len(fila)):
            hoja.write(i, c, fila[c])
    archivo.close()
    
    sleep(10)
    shutil.move ('directorio-ip.xlsx', "C:/Users/Public/Documents")
    lable_var('se a creado un excel en la carpeta DOCUMENTOS PUBLICOS')


# colores
Celeste = 'cadetblue1'
celeste = 'SkyBlue1'
negro = 'grey2'
blanco = 'ghost white'
oro = 'gold'

color_botones= negro
letras_botones = blanco

#↓ configuracion de la ventana
Tam_Vent = "900x500"
Titulo = "Listado de IP"
ventana = tk.Tk()
ventana.title(Titulo)
ventana.geometry(Tam_Vent)
ventana.configure(background=Celeste)
tam_v = [900, 500]

#↓ Ruda de almacenado de las imágenes
ruta_imagenes = '.\\Libreta IP\\Fondos\\'

#↓ imagen de  fondo para la ventana
fond_vent = [camb_imag(ruta_imagenes+'fondo.gif', tam_v[0], tam_v[1]), camb_imag(ruta_imagenes+'fondo2.gif', tam_v[0], tam_v[1]), camb_imag(ruta_imagenes+'fondo3.gif', tam_v[0], tam_v[1]),]
fondo_ventana = tk.Label(ventana, image=fond_vent[imagen[0]])
fondo_ventana.pack()

# ↓ stringvar, se guardan los datos entregados
equipos = tk.StringVar()
ipv4 = tk.StringVar()
ipv6 = tk.StringVar()
mac_addr = tk.StringVar()
usser = tk.StringVar()
tipo_e = tk.StringVar()
# ↑ esta aproposito para que no interfiera con el codigo

#↓ lugar donde estan las etiquetas y entradas
        # ↓ pociciones en Y de las entradas
Y_entr = [100, 175]
        # ↓ pociciones en Y de las etiquetas
Y_etiqu = [75, 150]
        # ↓ pociciones en x de las etiquetas y entradas
X_pos = [10, 197, 383, 569, 665, 773]

# ↓ tamaño y fuente de la letra usada
Tam_y_Letr = ('vladimir', 12)
tam_letr_bot = ('vladimir', 18)

# ↓ comienso de la ventana
etiq_titulo = tk.Label(ventana, text='Almacenamiento de Datos de Dispositivos') 
etiq_titulo.place(x=110, y=14)
etiq_titulo.config (fg=blanco,
                    bg=negro,
                 font=Tam_y_Letr)

# ↓ etiqueta sirve para identificar donde va el nombre del dispositivo
etiq_disp = tk.Label(ventana, text='↓ Nombre del dispositivo') 
etiq_disp.place(x=X_pos[0], y=Y_etiqu[0])
etiq_disp.config(fg=blanco,
                bg=negro,
                font=Tam_y_Letr)

# ↓ entrada de nombre del dispositivo
entr_disp = tk.Entry(ventana, textvariable=equipos)
entr_disp.place(x=X_pos[0], y=Y_entr[0])
entr_disp.config(font=Tam_y_Letr)

# ↓ etiquetas que marca la entrada de la direccion ip
etiq_ipv4 = tk.Label(ventana, text='↓ IPv4')  
etiq_ipv4.place(x=X_pos[1], y=Y_etiqu[0])
etiq_ipv4.config(fg=blanco,
                bg=negro,
                font=Tam_y_Letr)

# ↓ entrada de la ipv4
entr_ipv4 = tk.Entry(ventana, textvariable=ipv4)
entr_ipv4.place(x=X_pos[1], y=Y_entr[0])
entr_ipv4.config(font=Tam_y_Letr)

# ↓ etiquetas que marca la entrada de la direccion ipv6
etiq_ipv6 = tk.Label(ventana, text='↓ IPv6')  
etiq_ipv6.place(x=X_pos[2], y=Y_etiqu[0])
etiq_ipv6.config(fg=blanco,
                bg=negro,
                font=Tam_y_Letr)

# ↓ entrada de la ipv6
entr_ipv6 = tk.Entry(ventana, textvariable=ipv6)
entr_ipv6.place(x=X_pos[2], y=Y_entr[0])
entr_ipv6.config(font=Tam_y_Letr)

# ↓ etiquetas que marca la entrada de la mac addres
etiq_mac = tk.Label(ventana, text='↓ Mac Address')  
etiq_mac.place(x=X_pos[0], y=Y_etiqu[1])
etiq_mac.config(fg=blanco,
                bg=negro,
                font=Tam_y_Letr)

# ↓ entrada de la mac addres
entr_mac = tk.Entry(ventana, textvariable=mac_addr)
entr_mac.place(x=X_pos[0], y=Y_entr[1])
entr_mac.config(font=Tam_y_Letr)

# ↓ etiquetas que marca la entrada los usuarios
etiq_user = tk.Label(ventana, text='↓ Usuarios')  
etiq_user.place(x=X_pos[1], y=Y_etiqu[1])
etiq_user.config(fg=blanco,
                bg=negro,
                font=Tam_y_Letr)

# ↓ entrada de los usuarios
entr_user = tk.Entry(ventana, textvariable=usser)
entr_user.place(x=X_pos[1], y=Y_entr[1])
entr_user.config(font=Tam_y_Letr)

# ↓ etiquetas que marca la entrada los usuarios
etiq_user = tk.Label(ventana, text='↓ Dispositivo')  
etiq_user.place(x=X_pos[2], y=Y_etiqu[1])
etiq_user.config(fg=blanco,
                bg=negro,
                font=Tam_y_Letr)

# ↓ entrada de los usuarios
entr_user = tk.Entry(ventana, textvariable=tipo_e)
entr_user.place(x=X_pos[2], y=Y_entr[1])
entr_user.config(font=Tam_y_Letr) 

# ↓ boton de guardado 
boton_guardado = tk.Button(ventana, text='Guardar', command=guardar)
boton_guardado.place(x=(X_pos[3] + 4), y=(Y_etiqu[0] + 1))
boton_guardado.config(fg=blanco,
                    bg=color_botones,
                    font=tam_letr_bot)

# ↓ boton de editar
boton_editar = tk.Button(ventana, text='Editar', command=edit_datos)
boton_editar.place(x=(X_pos[4] + 20), y=(Y_etiqu[0] + 1))
boton_editar.config(fg=blanco,
                    bg=color_botones,
                    font=tam_letr_bot)

# ↓ boton para borrar( esto con un pop solo sirve)
boton_borrar = tk.Button(ventana, text=' Borrar  ', command=borrar_datos)
boton_borrar.place(x=(X_pos[3] + 4), y=(Y_etiqu[1] + 1))
boton_borrar.config(fg=blanco,
                    bg=color_botones,
                    font=tam_letr_bot)

# ↓ crear un exel con los datos.
boton_exel = tk.Button(ventana, text='Excel ', command=Crear_excel )
boton_exel.place(x=(X_pos[4] + 20), y=(Y_etiqu[1] + 1))
boton_exel.config(fg=blanco,
                    bg=color_botones,
                    font=tam_letr_bot)

# ↓ crear un exel con los datos.
boton_ping = tk.Button(ventana, text='Ping IPv4', command=ping_ipv4)
boton_ping.place(x=X_pos[5], y=(Y_etiqu[0] + 1))
boton_ping.config(fg=blanco,
                    bg=color_botones,
                    font=tam_letr_bot)

# ↓ crear un exel con los datos.
boton_ping = tk.Button(ventana, text='Ping IPv6', command=ping_ipv6)
boton_ping.place(x=X_pos[5], y=(Y_etiqu[1] + 1))
boton_ping.config(fg=blanco,
                    bg=color_botones,
                    font=tam_letr_bot)

flecha = Image.open(ruta_imagenes+'flecha-derecha.png')
flecha_izquierda = flecha.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
flecha_derecha = ImageTk.PhotoImage(flecha.resize((20, 20)))
flecha_izquierda = ImageTk.PhotoImage(flecha_izquierda.resize((20, 20)))

# ↓ boton de cambiar imágenes
boton_derecha = tk.Button(ventana, image=flecha_derecha, command=lambda: cambiar_fondo(1))
boton_derecha.place(x=870, y=211)
boton_derecha.config(bg=oro)
boton_izquierda = tk.Button(ventana, image=flecha_izquierda, command=lambda: cambiar_fondo(-1))
boton_izquierda.place(x=3, y=211)
boton_izquierda.config(bg=oro)

### -- terminamos con los botones y empezamos con la tabla

pos_y_tabl = 250
pos_x_tabl = 30

tbl = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4", "col5", "col6"))

tbl.column("#0", width=50)
tbl.column("col1", width=130)
tbl.column("col2", width=130)
tbl.column("col3", width=130)
tbl.column("col4", width=130)
tbl.column("col5", width=130)
tbl.column("col6", width=130)

tbl.heading("#0", text="")
tbl.heading("col1",text="Nombre")
tbl.heading("col2", text="IPv4")
tbl.heading("col3", text="IPv6")
tbl.heading("col4", text="Mac Addres")
tbl.heading("col5", text="Usuario")
tbl.heading("col6", text="Dispositivo")
tbl.place(x=pos_x_tabl, y=pos_y_tabl)

tbl.bind('<Double 1>', subir_columna)
actualizar_tabla()

ventana.resizable(width=False, height=False)
ventana.mainloop()