import tkinter as tk
#↑ importamos tkinter y lo llamamos tk para abreviar
# despues traemos todos lo que usamos con from e import.

# colores
Celeste = 'cadetblue1'
Azul_Cielo = 'SkyBlue1'

#↓ configuracion de la ventana
Tam_Vent = "810x800"                      
Titulo = "listado de ip"                          
ventana = tk.Tk()                         
ventana.title(Titulo)                     
ventana.geometry(Tam_Vent)                
ventana.configure (background= Celeste)   


# ↓ stringvar, se guardan los datos entregados
equipos = tk.StringVar()
ipv4 = tk.StringVar()
ipv6 = tk.StringVar ()
mac_addr = tk.StringVar ()
usser = tk.StringVar ()
# ↑ esta aproposito para que no interfiera con el codigo

#↓ lugar donde estan las etiquetas y entradas
        # ↓ pociciones en Y de las entradas
Y_entr = [75, 125,]
        # ↓ pociciones en Y de las etiquetas
Y_etiqu = [50, 100,]
        # ↓ pociciones en x de las etiquetas y entradas
X_pos = [15, 202, 388, 574, 670,]

# ↓ tamaño y fuente de la letra usada
Tam_y_Letr = ('vladimir', 12)
tam_letr_bot = ('vladimir', 18)

# ↓ comienso de la ventana
etiq_titulo = tk.Label (ventana, text= 'almacenamiento de datos de dispositivos') 
etiq_titulo.place(x=60, y=5,)
etiq_titulo.config (bg= Celeste,
                    font= ("Verdana", 24,),)

# ↓ etiqueta sirve para identificar donde va el nombre del dispositivo
etiq_disp = tk.Label (ventana, text= '↓ nombre del dispositivo') 
etiq_disp.place(x=X_pos [0], y=Y_etiqu [0],)
etiq_disp.config ( bg= Azul_Cielo,
                    font= Tam_y_Letr)

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
etiq_ipv6 = tk.Label (ventana, text= '↓ ip version 6')  
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

# ↓ boton de guardado 
boton_guardado = tk.Button(ventana, text= 'guardar')
boton_guardado.place (x=(X_pos[2] +4 ), y= Y_etiqu [1],)
boton_guardado.config(bg= Azul_Cielo,
                    font= tam_letr_bot)

# ↓ boton de editar ( crear un pop para borrar y reguardar)
boton_editar = tk.Button(ventana, text= 'editar')
boton_editar.place (x=(X_pos[3] +4 ), y= Y_etiqu [0],)
boton_editar.config(bg= Azul_Cielo,
                    font= tam_letr_bot)

# ↓ boton para borrar ( esto con un pop solo sirve)
boton_borrar = tk.Button(ventana, text= 'borrar')
boton_borrar.place (x=(X_pos[3] +4 ), y= Y_etiqu [1],)
boton_borrar.config(bg= Azul_Cielo,
                    font= tam_letr_bot )

# ↓ crear un exel con los datos.
boton_exel = tk.Button(ventana, text= 'crear exel')
boton_exel.place (x= X_pos[4], y= Y_etiqu [1],)
boton_exel.config(bg= Azul_Cielo,
                    font= tam_letr_bot )

# ↓ crear un exel con los datos.
boton_ping = tk.Button(ventana, text= 'ping')
boton_ping.place (x= X_pos[4], y= Y_etiqu [0],)
boton_ping.config(bg= Azul_Cielo,
                    font= tam_letr_bot )

# accion del boton "ping" (no pude hacer que el usuario ingrese una variable o un input)
import subprocess
import platform


def ping(host):
    parametro = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping',parametro,'4',host]
   
    subprocess.call(comando)


ping('192.168.0.1')


ventana.mainloop()
