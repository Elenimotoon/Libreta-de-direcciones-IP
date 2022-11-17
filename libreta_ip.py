import tkinter as tk
#↑ importamos tkinter y lo llamamos tk para abreviar
# despues traemos todos lo que usamos con from e import.
from tkinter import ttk
# ↑ tambien importamos la libreria ttk que nos permite hacer tablas.
from PIL import ImageTk, Image
# ↑ PIL es una libreria para redimencionar imagenes
from cont_bdata import *


#↓ configuracion de los botones    
def guardar():
    col1 = equipos.get()
    col2 = ipv4.get()
    col3 = ipv6.get() 
    col4 = mac_addr.get() 
    col5 = usser.get() 
    col6 = tipo_e.get()  


def camb_imag (imagn, tam1, tam2):
    imag_entr = Image.open(imagn)
    imag_entr = imag_entr.resize((tam1, tam2), Image.ANTIALIAS)
    imag_sal = ImageTk.PhotoImage(imag_entr)
    return imag_sal

# colores
Celeste = 'cadetblue1'
Azul_Cielo = 'SkyBlue1'

#↓ configuracion de la ventana
Tam_Vent = "900x500"                      
Titulo = "listado de ip"                          
ventana = tk.Tk()                         
ventana.title(Titulo)                     
ventana.geometry(Tam_Vent)                
ventana.configure (background= Celeste)

#↓ imagen de  fondo para la ventana
fond_vent = [camb_imag('fondo.gif', 900, 500), camb_imag('fondo2.gif', 900, 500), camb_imag('fondo3.gif', 900, 500),]

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
fondo_ventana = tk.Label(ventana, image= fond_vent[1])
fondo_ventana.pack()
# ↓ comienso de la ventana
etiq_titulo = tk.Label (ventana, text= 'almacenamiento de datos de dispositivos') 
etiq_titulo.place(x=60, y=5,)
etiq_titulo.config (bg= Celeste,
                    font= ("Verdana", 24,),)

# ↓ imagenes de las etiquetas
tam_botones = [100, 30,]
botones = [camb_imag('boton-guardar.gif', tam_botones[0], tam_botones[1]), camb_imag('boton-editar.gif',tam_botones[0], tam_botones[1]),
            camb_imag('boton-eliminar.gif',tam_botones[0], tam_botones[1]), camb_imag('boton-excel.gif', tam_botones[0], tam_botones[1]),
            camb_imag('boton-ping-ipv4.gif', tam_botones[0], tam_botones[1]), camb_imag('boton-ping-ipv6.gif', tam_botones[0], tam_botones[1]),]


# ↓ etiqueta sirve para identificar donde va el nombre del dispositivo
etiq_disp = tk.Label (ventana, texto= 'nombre del dispositivo') 
etiq_disp.place(x=X_pos [0], y=Y_etiqu [0],)


# ↓ entrada de nombre del dispositivo
entr_disp = tk.Entry (ventana, textvariable= equipos, ) 
entr_disp.place (x= X_pos [0], y= Y_entr [0])
entr_disp.config(font= Tam_y_Letr)

# ↓ etiquetas que marca la entrada de la direccion ip
etiq_ipv4 = tk.Label (ventana, text= '↓ ip version 4')  
etiq_ipv4.place(x=X_pos[1], y= Y_etiqu [0],)
etiq_ipv4.config(bg= Azul_Cielo,
                    font= Tam_y_Letr)

# ↓ entrada de la ipv4
entr_ipv4 = tk.Entry (ventana, textvariable= ipv4, )
entr_ipv4.place (x=X_pos[1], y=Y_entr [0],)
entr_ipv4.config(font= Tam_y_Letr)

# ↓ etiquetas que marca la entrada de la direccion ipv6
etiq_ipv6 = tk.Label (ventana, text= 'ipv6')  
etiq_ipv6.place(x=X_pos[2], y= Y_etiqu [0],)
etiq_ipv6.config(bg= Azul_Cielo,
                    font= Tam_y_Letr)

# ↓ entrada de la ipv6
entr_ipv6 = tk.Entry (ventana, textvariable= ipv6, )
entr_ipv6.place (x=X_pos[2], y=Y_entr [0],)
entr_ipv6.config(font= Tam_y_Letr)

# ↓ etiquetas que marca la entrada de la mac addres
etiq_mac = tk.Label (ventana, text= '↓ mac addres')  
etiq_mac.place(x=X_pos[0], y= Y_etiqu [1],)
etiq_mac.config(bg= Azul_Cielo,
                    font= Tam_y_Letr)

# ↓ entrada de la mac addres
entr_mac = tk.Entry (ventana, textvariable= mac_addr, )
entr_mac.place (x=X_pos[0], y=Y_entr [1],)
entr_mac.config(font= Tam_y_Letr)

# ↓ etiquetas que marca la entrada los usuarios
etiq_user = tk.Label (ventana, text= '↓ usuarios')  
etiq_user.place(x=X_pos[1], y= Y_etiqu [1],)
etiq_user.config(bg= Azul_Cielo,
                    font= Tam_y_Letr)

# ↓ entrada de los usuarios
entr_user = tk.Entry (ventana, textvariable= usser, )
entr_user.place (x=X_pos[1], y=Y_entr [1],)
entr_user.config(font= Tam_y_Letr)

# ↓ etiquetas que marca la entrada los usuarios
etiq_user = tk.Label (ventana, text= '↓ dispositivo')  
etiq_user.place(x=X_pos[2], y= Y_etiqu [1],)
etiq_user.config(bg= Azul_Cielo,
                    font= Tam_y_Letr)

# ↓ entrada de los usuarios
entr_user = tk.Entry (ventana, textvariable= tipo_e, )
entr_user.place (x=X_pos[2], y=Y_entr [1],)
entr_user.config(font= Tam_y_Letr) 

# ↓ boton de guardado 
boton_guardado = tk.Button(ventana, image= botones [0], command= guardar)
boton_guardado.place (x=(X_pos[3] +4 ), y= Y_etiqu [0],)


# ↓ boton de editar ( crear un pop para borrar y reguardar)
boton_editar = tk.Button(ventana, image= botones [1],)
boton_editar.place (x=(X_pos[4] +20 ), y= Y_etiqu [0],)


# ↓ boton para borrar ( esto con un pop solo sirve)
boton_borrar = tk.Button(ventana, image= botones [2],)
boton_borrar.place (x=(X_pos[3] +4 ), y= Y_etiqu [1],)


# ↓ crear un exel con los datos.
boton_exel = tk.Button(ventana, image= botones [3],)
boton_exel.place (x= (X_pos[4] +20 ), y= Y_etiqu [1],)


# ↓ crear un exel con los datos.
boton_ping = tk.Button(ventana, image= botones [4],)
boton_ping.place (x= X_pos[5], y= Y_etiqu [0],)


# ↓ crear un exel con los datos.
boton_ping = tk.Button(ventana, image= botones [5],)
boton_ping.place (x= X_pos[5], y= Y_etiqu [1],)


### -- terminamos con los botones y empezamos con la tabla

pos_y_tabl = 250
pos_x_tabl = 30

tbl = ttk.Treeview(ventana, columns= ("col1", "col2", "col3", "col4", "col5", "col6",),)

tbl.column("#0", width=50)
tbl.column("col1", width=130,)
tbl.column("col2", width=130,)
tbl.column("col3", width=130,)
tbl.column("col4", width=130,)
tbl.column("col5", width=130,)
tbl.column("col6", width=130,)

tbl.heading("#0", text="",)
tbl.heading("col1",text= "nombre",)
tbl.heading("col2", text="ipv4", )
tbl.heading("col3", text= "ipv6",)
tbl.heading("col4", text= "mac addres")
tbl.heading("col5", text= "usuario")
tbl.heading("col6", text= "dispositivo")
tbl.place(x=pos_x_tabl, y=pos_y_tabl)


ventana.resizable(width=False, height=False)
ventana.mainloop()