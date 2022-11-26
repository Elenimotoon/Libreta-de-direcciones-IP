import tkinter as tk
#↑ importamos tkinter y lo llamamos tk para abreviar
# despues traemos todos lo que usamos con from e import.
from tkinter import ttk
# ↑ tambien importamos la libreria ttk que nos permite hacer tablas.
from cont_bdata import *
from PIL import ImageTk, Image

# ↑ esta es la base de datos para guardar o importar los datos
from ipaddress import ip_address
# ↑ es para comprobar y validar la ip
from time import sleep
from platform import system
from subprocess import call

def ping (host):
    parametro = '-n' if system ().lower() == 'windows' else '-c' 
    comando = ['ping', parametro, '1', host] 
    devol = call (comando)
    return devol
        

# esta es una etiqueta que desaparece.
def lable_var (pal_var, pos_x= 15, pos_y = 475):
    texto = pal_var
    etiq_var = tk.Label (ventana, text= texto)  
    etiq_var.place(x= pos_x, y=pos_y,)
    etiq_var.config(fg=blanco,
                bg= negro,
                font= Tam_y_Letr)
    etiq_user.after(3000, lambda: etiq_var.destroy())
    #↑ esta linea desaparece la etiqueta


def camb_imag (imagn, tam1, tam2):
    imag_entr = Image.open(imagn)
    imag_entr = imag_entr.resize((tam1, tam2), Image.ANTIALIAS)
    imag_sal = ImageTk.PhotoImage(imag_entr)
    return imag_sal

# ↓ es para que muestre si la ip es valida
def validate_ip_address(ip_string):
   try:
       ip_object = ip_address(ip_string)
       return f"la ip {ip_object} existe"
   except ValueError:
       return f"la ip {ip_string} no existe"


def ping_ipv6 ():
    col3 = ipv6.get() 
    validacion = validate_ip_address (col3)
    lable_var(validacion)
    sleep (3)
    devol = ping(col3)
    lable_var (devol)


def ping_ipv4 ():
    col2 = ipv4.get()
    validacion = validate_ip_address (col2)
    lable_var(validacion)
    sleep (3)
    devol = ping(col2)
    if devol == 0:
        lable_var (f'la ip {col2} esta en uso')
    elif devol != 0:
        lable_var(f'la ip {col2} no esta conectada')
    
def borrar_datos():
    col1 = equipos.get
    eliminar_filas(col1)
    lable_var(f'{col1} fue eliminado')


#↓ configuracion de los botones    
def guardar():
    col1 = equipos.get()
    col2 = ipv4.get()
    col3 = ipv6.get() 
    col4 = mac_addr.get() 
    col5 = usser.get() 
    col6 = tipo_e.get()
    ins_datos(col1, col2, col3, col4, col5, col6,)
    col1 = equipos.set("")
    col2 = ipv4.set("")
    col3 = ipv6.set("")
    col4 = mac_addr.set("")
    col5 = usser.set("")
    col6 = tipo_e.set("") 
    lable_var('datos guardados')
    

#↓ esto guarda los elementos en la lista de ventana.
def actualizar_tabla ():
    lista_cruda = leer_datos ()
    len_lista = len(lista_cruda)
    vueltas = 0
    elem_tabl = tbl.get_children()
    for elemento in elem_tabl :
        tbl.delete(elemento)
    while not len_lista == vueltas :
        columnas = list (lista_cruda[vueltas])
        col1 = columnas[0]
        col2 = columnas[1]
        col3 = columnas[2]
        col4 = columnas[3]
        col5 = columnas[4]
        col6 = columnas[5]
        tbl.insert("",tk.END ,text= '', values=(col1, col2, col3, col4, col5, col6,))
        vueltas +=1
    lable_var('lista actualizada')


def edit_datos ():
    eliminar_filas(col1)
    col1 = equipos.get()
    col2 = ipv4.get()
    col3 = ipv6.get() 
    col4 = mac_addr.get() 
    col5 = usser.get() 
    col6 = tipo_e.get()
    editar_datos(col1, col2, col3, col4, col5, col6,)
    col1 = equipos.set("")
    col2 = ipv4.set("")
    col3 = ipv6.set("")
    col4 = mac_addr.set("")
    col5 = usser.set("")
    col6 = tipo_e.set("") 
    lable_var('datos guardados')

# colores
Celeste = 'cadetblue1'
celeste = 'SkyBlue1'
negro = 'grey2'
blanco = 'ghost white'

color_botones= negro
letras_botones = blanco
#↓ configuracion de la ventana
Tam_Vent = "900x500"                      
Titulo = "listado de ip"                          
ventana = tk.Tk()                         
ventana.title(Titulo)                     
ventana.geometry(Tam_Vent)                
ventana.configure (background= Celeste)
tam_v = [900, 500]

fond_vent = [camb_imag('fondo.gif', tam_v[0], tam_v[1]), camb_imag('fondo2.gif', tam_v[0], tam_v[1]), camb_imag('fondo3.gif',tam_v[0], tam_v[1]),]
fondo_ventana = tk.Label(ventana, image= fond_vent[2])
fondo_ventana.pack()

#↓ imagen de  fondo para la ventana

# ↓ stringvar, se guardan los datos entregados
equipos = tk.StringVar()
ipv4 = tk.StringVar()
ipv6 = tk.StringVar ()
mac_addr = tk.StringVar ()
usser = tk.StringVar ()
tipo_e = tk.StringVar()
# ↑ esta aproposito para que no interfiera con el codigo

#↓ lugar donde estan las etiquetas y entradas
        # ↓ pociciones en Y de las entradas
Y_entr = [100, 175,]
        # ↓ pociciones en Y de las etiquetas
Y_etiqu = [70, 150,]
        # ↓ pociciones en x de las etiquetas y entradas
X_pos = [15, 202, 388, 574, 670, 780]

# ↓ tamaño y fuente de la letra usada
Tam_y_Letr = ('vladimir', 12)
tam_letr_bot = ('vladimir', 18)


# ↓ comienso de la ventana
fondo_ventana = tk.Label(ventana,)
fondo_ventana.pack()

# ↓ comienso de la ventana
etiq_titulo = tk.Label (ventana, text='almacenamiento de datos de dispositivos') 
etiq_titulo.place(x=60, y=5,)
etiq_titulo.config (bg= Celeste,
                    font= ("Verdana", 24,),)

# ↓ etiqueta sirve para identificar donde va el nombre del dispositivo
etiq_disp = tk.Label (ventana, text= ' ↓ nombre del dispositivo') 
etiq_disp.place(x=X_pos [0], y=Y_etiqu [0],)
etiq_disp.config(fg=blanco,
                 bg= negro,
                 font= Tam_y_Letr)

# ↓ entrada de nombre del dispositivo
entr_disp = tk.Entry (ventana, textvariable= equipos, ) 
entr_disp.place (x= X_pos [0], y= Y_entr [0])
entr_disp.config(font= Tam_y_Letr)

# ↓ etiquetas que marca la entrada de la direccion ip
etiq_ipv4 = tk.Label (ventana, text= '↓ ip v4')  
etiq_ipv4.place(x=X_pos[1], y= Y_etiqu [0],)
etiq_ipv4.config(fg=blanco,
                 bg= negro,
                 font= Tam_y_Letr)


# ↓ entrada de la ipv4
entr_ipv4 = tk.Entry (ventana, textvariable= ipv4, )
entr_ipv4.place (x=X_pos[1], y=Y_entr [0],)
entr_ipv4.config(font= Tam_y_Letr)

# ↓ etiquetas que marca la entrada de la direccion ipv6
etiq_ipv6 = tk.Label (ventana, text= ' ↓ ip v6')  
etiq_ipv6.place(x=X_pos[2], y= Y_etiqu [0],)
etiq_ipv6.config(fg=blanco,
                 bg= negro,
                 font= Tam_y_Letr)


# ↓ entrada de la ipv6
entr_ipv6 = tk.Entry (ventana, textvariable= ipv6, )
entr_ipv6.place (x=X_pos[2], y=Y_entr [0],)
entr_ipv6.config(font= Tam_y_Letr)

# ↓ etiquetas que marca la entrada de la mac addres
etiq_mac = tk.Label (ventana, text= '↓ mac addres')  
etiq_mac.place(x=X_pos[0], y= Y_etiqu [1],)
etiq_mac.config(fg=blanco,
                 bg= negro,
                 font= Tam_y_Letr)


# ↓ entrada de la mac addres
entr_mac = tk.Entry (ventana, textvariable= mac_addr, )
entr_mac.place (x=X_pos[0], y=Y_entr [1],)
entr_mac.config(font= Tam_y_Letr)

# ↓ etiquetas que marca la entrada los usuarios
etiq_user = tk.Label (ventana, text= '↓ usuarios')  
etiq_user.place(x=X_pos[1], y= Y_etiqu [1],)
etiq_user.config(fg=blanco,
                 bg= negro,
                 font= Tam_y_Letr)


# ↓ entrada de los usuarios
entr_user = tk.Entry (ventana, textvariable= usser, )
entr_user.place (x=X_pos[1], y=Y_entr [1],)
entr_user.config(font= Tam_y_Letr)

# ↓ etiquetas que marca la entrada los usuarios
etiq_user = tk.Label (ventana, text= '↓ dispositivo')  
etiq_user.place(x=X_pos[2], y= Y_etiqu [1],)
etiq_user.config(fg=blanco,
                 bg= negro,
                 font= Tam_y_Letr)


# ↓ entrada de los usuarios
entr_user = tk.Entry (ventana, textvariable= tipo_e, )
entr_user.place (x=X_pos[2], y=Y_entr [1],)
entr_user.config(font= Tam_y_Letr) 

# ↓ boton de guardado 
boton_guardado = tk.Button(ventana, text= 'guardar', command= guardar)
boton_guardado.place (x=(X_pos[3] +4 ), y= Y_etiqu [0],)
boton_guardado.config(fg=blanco,
                    bg= color_botones,
                    font= tam_letr_bot)

# ↓ boton de editar
boton_editar = tk.Button(ventana, text= 'editar',)
boton_editar.place (x=(X_pos[4] +20 ), y= Y_etiqu [0],)
boton_editar.config(fg=blanco,
                    bg= color_botones,
                    font= tam_letr_bot)

# ↓ boton para borrar ( esto con un pop solo sirve)
boton_borrar = tk.Button(ventana, text= ' borrar ', command= borrar_datos)
boton_borrar.place (x=(X_pos[3] +4 ), y= Y_etiqu [1],)
boton_borrar.config(fg=blanco,
                    bg= color_botones,
                    font= tam_letr_bot )

# ↓ crear un exel con los datos.
boton_exel = tk.Button(ventana, text= ' exel ')
boton_exel.place (x= (X_pos[4] +20 ), y= Y_etiqu [1],)
boton_exel.config(fg=blanco,
                    bg= color_botones,
                    font= tam_letr_bot )

# ↓ crear un exel con los datos.
boton_ping = tk.Button(ventana, text= 'ping ipv4', command= ping_ipv4)
boton_ping.place (x= X_pos[5], y= Y_etiqu [0],)
boton_ping.config(fg=blanco,
                    bg= color_botones,
                    font= tam_letr_bot )

# ↓ crear un exel con los datos.
boton_ping = tk.Button(ventana, text= 'ping ipv6', command= ping_ipv6)
boton_ping.place (x= X_pos[5], y= Y_etiqu [1],)
boton_ping.config(fg=blanco,
                    bg= color_botones,
                    font= tam_letr_bot )

# ↓ boton de actualizar.
boton_ping = tk.Button(ventana, text= 'actualizar',command= actualizar_tabla)
boton_ping.place (x= 800, y= 220,)
boton_ping.config(fg=blanco,
                bg= color_botones,
                    font= ('vladimir', 8))

### -- terminamos con los botones y empezamos con la tabla

pos_y_tabl = 250
pos_x_tabl = 30

tbl = ttk.Treeview(ventana, columns= ("col1", "col2", "col3", "col4", "col5", "col6",),)
actualizar_tabla()

tbl.column("#0", width=50)
tbl.column("col1", width=130,)
tbl.column("col2", width=130,)
tbl.column("col3", width=130,)
tbl.column("col4", width=130,)
tbl.column("col5", width=130,)
tbl.column("col6", width=130,)

tbl.heading("#0", text='',)
tbl.heading("col1",text= "nombre",)
tbl.heading("col2", text="ipv4", )
tbl.heading("col3", text= "ipv6",)
tbl.heading("col4", text= "mac addres")
tbl.heading("col5", text= "usuario")
tbl.heading("col6", text= "dispositivo")
tbl.place(x=pos_x_tabl, y=pos_y_tabl)


ventana.resizable(width=False, height=False)
ventana.mainloop()