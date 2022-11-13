from tkinter import *
from tkinter import messagebox

lista = []

def guardar():
    n = nombre.get()
    ap = app.get()
    am = apm.get()
    c = correo.get()
    t = telefono.get()
    lista.append(n+"$"+ap+"$"+am+"$"+c+"$"+t)
    escribirContacto()
    messagebox.showinfo("Guardado","El contacto ha sido guardado en la agenda")
    nombre.set('')
    app.set('')
    apm.set('')
    correo.set('')
    telefono.set('')
    consultar()

def eliminar():
    eliminado = conteliminar.get()
    removido = False
    for elemento in lista:
        array = elemento.split("$")
        if conteliminar.get() == array[3]:
            lista.remove(elemento)
            removido = True
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar","Elemento eliminado"+eliminado)

def consultar():
    r = Text(ventana,width=80,height=15)
    lista.sort()
    valores = []
    r.insert(INSERT,"Nombre\t\tApellido P\t\tApellido M\t\tTelefono\t\tCorreo\n")
    for elemento in lista:
        array = elemento.split("$")
        valores.append(array[3])
        r.insert(INSERT,array[0]+"\t\t"+array[1]+"\t\t"+array[2]+"\t\t"+array[3]+"\t\t"+array[4]+"\n")
    r.place(x=20,y=230)
    spinTelefono = Spinbox(ventana,value=(valores),textvariable=conteliminar).place(x=450,y=50)
    if lista==[]:
        spinTelefono = Spinbox(ventana,value=(valores)).place(x=450,y=50)
    r.config(state=DISABLED)

def inciarArchivo():
    archivo = open("ag.txt","a")
    archivo.close()

def cargar():
    archivo = open("ag.txt","r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

def escribirContacto():
    archivo = open("ag.txt","w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+'\n')
        archivo.close()

ventana = Tk()
nombre = StringVar()
app = StringVar()
apm = StringVar()
correo = StringVar()
telefono = StringVar()
conteliminar = StringVar()
colorFondo = "#006"
colorLetra = "#FFF"
inciarArchivo()
cargar()
consultar()
ventana.title("Agenda con archivos")
ventana.geometry("700x500")
ventana.configure(background=colorFondo)
etiquetaTitlulo = Label(ventana,text="Agenda con Archivos",bg=colorFondo,fg=colorLetra,font=("Helvetica", 16)).place(x=230,y=10)
etiquetaNombre = Label(ventana,text="Nombre: ",bg=colorFondo,fg=colorLetra).place(x=50,y=50)
cajaNombre = Entry(ventana,textvariable=nombre).place(x=150,y=50)
etiquetApp = Label(ventana,text="Apellido Paterno: ",bg=colorFondo,fg=colorLetra).place(x=50,y=80)
cajApp = Entry(ventana,textvariable=app).place(x=150,y=80)
etiquetApm = Label(ventana,text="Apellido Materno: ",bg=colorFondo,fg=colorLetra).place(x=50,y=110)
cajApm = Entry(ventana,textvariable=apm).place(x=150,y=110)
etiquetT = Label(ventana,text="Teléfono: ",bg=colorFondo,fg=colorLetra).place(x=50,y=140)
cajT = Entry(ventana,textvariable=telefono).place(x=150,y=140)
etiquetC = Label(ventana,text="Correo: ",bg=colorFondo,fg=colorLetra).place(x=50,y=170)
cajC = Entry(ventana,textvariable=correo).place(x=150,y=170)
etiquetaEliminar = Label(ventana,text="Teléfono: ",bg=colorFondo,fg=colorLetra).place(x=370,y=50)
spinTelefono = Spinbox(ventana,textvariable=conteliminar).place(x=450,y=50)
botonGuardar = Button(ventana,text="Guardar",command=guardar,bg='#009',fg="white").place(x=180,y=200)
botonEliminar = Button(ventana,text="Eliminar",command=eliminar,bg="#009",fg="white").place(x=470,y=80)
mainloop()