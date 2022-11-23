from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

prueba = [['Titulo', 'El mundo se acaba..'], ['Vida Máxima', '18'], ['Historia', 'Había una vez... truz']]

def update(prueba):
    for i in prueba:
        trv.insert('', 'end', values=i, tags='unchecked')

def getrow(event):
    row_id = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    if item['values'][0] == "Titulo":
        caja_titulo.set(item['values'][1])
    if item['values'][0] == "Vida Máxima":
        caja_vida_max.set(item['values'][1])
    if item['values'][0] == "Historia":
        caja_historia.set(item['values'][1])

def aniadir_nodo():
    titulo = caja_titulo.get()
    vida_max = caja_vida_max.get()
    historia = caja_historia.get()
    
    if titulo == '':
        titulo = None
    if not vida_max.isnumeric() or vida_max == "0":
        return messagebox.showerror("Error de lectura", "Por favor, revise los datos ingresados y vuelva a intentarlo")
    if historia == '':
        historia = None
    
    print(prueba)
    prueba.append(['Titulo', titulo])
    prueba.append(['Vida Máxima', vida_max])
    prueba.append(['Historia', historia])
    update(prueba)
    print(prueba)
    messagebox.showinfo("Guardado", "¡Nodo guardado exitosamente!")

def actualizar_nodo():
    titulo = caja_titulo.get()
    vida_max = caja_vida_max.get()
    historia = caja_historia.get()
    item = trv.item(trv.focus())
    if len(item['values']) == 0:
        return messagebox.showerror("Error", "No se a proporcionado un nodo a actualizar")
    if messagebox.askyesno("Advertencia", f"¡Está apunto de cambiar los valores de {item['values'][0]}!\n\n¿Está seguro de hacerlo?"):
        print("Valores Modificados")
    else:
        return True

def borrar_nodo():
    row_id = caja_titulo.get()
    item = trv.item(trv.focus())
    print(item)
    if len(item['values']) == 0:
        return messagebox.showerror("Error", "No se a proporcionado un nodo a eliminar")
    if messagebox.askyesno("Advertencia", "¡Si elimina este nodo no habrá vuelta atrás!\n\n¿Está seguro?"):
        print("Nodo eliminado...")
    return True

def ventana_reglas():
    reglas = Toplevel(ventana)
    reglas.geometry("250x250")
    reglas.title("Reglas")
    reglas.resizable(False, False)
    descripcion = Label(reglas, text="Estas son las reglas")
    descripcion.pack()
    cerrar = Button(reglas, text="Cerrar", command=lambda: reglas.destroy())
    cerrar.pack()

ventana = Tk()
caja_titulo = StringVar()
caja_vida_max = StringVar()
caja_historia = StringVar()

# Menu Bar
menubar = Menu(ventana)
archivo_menu = Menu(menubar, tearoff=0)
archivo_menu.add_command(label="Formato Simple", command=lambda: print('Formato basico activado'))
archivo_menu.add_command(label="Formato Datallado", command=lambda: print('Formato pro activado'))
archivo_menu.add_command(label="Guardar", command=lambda: print('Guardando Archivo'))
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)
menubar.add_cascade(label="Archivo", menu=archivo_menu)

info_menu = Menu(menubar, tearoff=0)
info_menu.add_command(label="Reglas", command=ventana_reglas)
info_menu.add_command(label="Ejemplos", command=lambda: print("Mostando ejemplos"))
info_menu.add_command(label="Funcionamiento", command=lambda: print("Mostando funcionamiento"))
menubar.add_cascade(label="Info", menu=info_menu)

# Label
label_principal = Label(ventana)
label_principal.grid(row=0, column=0, padx=5, pady=3)

label_de_ayuda = Label(ventana)
label_de_ayuda.grid(row=0, column=1, padx=5, pady=3)

# Dentro
wrapper0 = LabelFrame(label_principal, text='Carpetitas')
wrapper1 = LabelFrame(label_de_ayuda, text='Visualizador')
wrapper2 = LabelFrame(label_de_ayuda, text='Modificador')

wrapper0.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

# Carpetitas
tv = ttk.Treeview(wrapper0)
item1 = tv.insert("", END, text="MAIN", open=1)
tv.insert(item1, END, text="TITLE")
item1 = tv.insert("", END, text="MENU", open=1)
tv.insert(item1, END, text="PLAY")
item1 = tv.insert("", END, text="HISTORY", open=1)
tv.insert(item1, END, text="PROLOG")
tv.pack()

img_checkeado = ImageTk.PhotoImage(Image.open("checked_box.svg"))
img_descheckeado = ImageTk.PhotoImage(Image.open("unchecked_box.svg"))

# Visualizador
trv = ttk.Treeview(wrapper1, columns=(1,2))
style = ttk.Style(trv)
style.configure('Treeview', rowheight=24)

trv.tag_configure('checked', image=img_checkeado)
trv.tag_configure('unchecked', image=img_descheckeado)

trv.pack()
trv.heading('#0', text="")
trv.heading('#1', text="Values")
trv.heading('#2', text="Estructura")

trv.bind('<Double 1>', getrow)

update(prueba)

# Modificador
eTitulo = Label(wrapper2, text="Titulo: ")
eTitulo.grid(row=0, column=0, padx=5, pady=3)

cTitulo = Entry(wrapper2, textvariable=caja_titulo)
cTitulo.grid(row=0, column=1, padx=5, pady=3)

eVidaM = Label(wrapper2, text="Vida Máxima: ")
eVidaM.grid(row=1, column=0, padx=5, pady=3)

cVidaM = Entry(wrapper2, textvariable=caja_vida_max)
cVidaM.grid(row=1, column=1, padx=5, pady=3)

eHistoria = Label(wrapper2, text="Historia: ")
eHistoria.grid(row=2, column=0, padx=5, pady=3)

cHistoria = Entry(wrapper2, textvariable=caja_historia)
cHistoria.grid(row=2, column=1, padx=5, pady=3)

boton_aniadir = Button(wrapper2, text="Añadir Nodo", command=aniadir_nodo)
boton_actualizar = Button(wrapper2, text="Actualizar Valor", command=actualizar_nodo)
boton_borrar = Button(wrapper2, text="Borrar Nodo", command=borrar_nodo)

boton_aniadir.grid(row=3, column=0, padx=5, pady=3)
boton_actualizar.grid(row=3, column=1, padx=5, pady=3)
boton_borrar.grid(row=3, column=2, padx=5, pady=3)

ventana.title("Editor Histórico")
ventana.geometry('750x350')
ventana.resizable(False, False)
ventana.config(menu=menubar)

ventana.mainloop()