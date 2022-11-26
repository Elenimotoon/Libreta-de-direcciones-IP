from tkinter import *
#import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
# Llamo las dependencia de Tkinter y Pillow que voy a utilizar

# Prueba de los valores que tendrían las columnas
prueba = [['Titulo', 'El mundo se acaba..'], ['Vida Máxima', 18], ['Historia', 'Había una vez... truz']]

# Actualizo las columnas con los valores almacenados
def update(prueba):
    for i in prueba:
        trv.insert('', 'end', values=i)

# Si la checkbox está marcada la desmarca y si está desmarcada la marca
def toggleCheck(event):
    row_id = tv.identify_row(event.y)
    if not row_id == '' and not tv.item(row_id, "tags") == '':
        tag = tv.item(row_id, "tags")[0]
        tags = list(tv.item(row_id, "tags"))
        tags.remove(tag)
        tv.item(row_id, tags=tags)
        if tag == "checked":
            tv.item(row_id, tags="unchecked")
        else:
            tv.item(row_id, tags="checked")

# Tomo los valores de las columnas y las paso a las casillas
# TODO A futuro editar esto
def getrow(event):
    row_id = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    if item['values'][0] == "Titulo":
        caja_titulo.set(item['values'][1])
    if item['values'][0] == "Vida Máxima":
        caja_vida_max.set(item['values'][1])
    if item['values'][0] == "Historia":
        caja_historia.set(item['values'][1])

# Añado los valores de las cajas a la columna
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
    
    # Elimino los valores de las columnas actuales
    trv.delete(*trv.get_children())
    
    prueba.append(['Titulo', titulo])
    prueba.append(['Vida Máxima', int(vida_max)])
    prueba.append(['Historia', historia])
    # Actualizo las columnas con los valores actuales
    update(prueba)
    
    # Limpio las cajas
    caja_titulo.set('')
    caja_vida_max.set('')
    caja_historia.set('')
    messagebox.showinfo("Guardado", "¡Nodo guardado exitosamente!")

# Actualizo los valores tanto para el JSON como para las columnas
# FIXME Aun sigo trabajando en esto
def actualizar_nodo():
    # titulo = caja_titulo.get()
    # vida_max = caja_vida_max.get()
    # historia = caja_historia.get()
    item = trv.item(trv.focus())
    if len(item['values']) == 0:
        return messagebox.showerror("Error", "No se a proporcionado un nodo a actualizar")
    
    # borrar_nodo()
    # aniadir_nodo()
    
    if messagebox.askyesno("Advertencia", f"¡Está apunto de cambiar los valores de {item['values'][0]}!\n\n¿Está seguro de hacerlo?"):
        # Temporal
        print("Valores Modificados")
    else:
        return True

# Borra el nodo seleccionado
def borrar_nodo():
    item_id = trv.focus()
    item = trv.item(item_id)
    if len(item['values']) == 0:
        return messagebox.showerror("Error", "No se a proporcionado un nodo a eliminar")
    if messagebox.askyesno("Advertencia", "¡Si elimina este nodo no habrá vuelta atrás!\n\n¿Está seguro?"):
        tags = list(trv.get_children())
        tags.remove(item_id)
        prueba.remove(item['values'])
        trv.delete(*trv.get_children())
        update(prueba)
        print("Nodo eliminado...")
    return True

# TODO Agreguen el resto de ventanas pls, acá tienen la base
# Muchos de los datos necesarios están en ReglasEstructura.md
def ventana_reglas():
    reglas = Toplevel(ventana)
    reglas.geometry("250x250")
    reglas.title("Reglas")
    reglas.resizable(False, False)
    descripcion = Label(reglas, text="Estas son las reglas")
    descripcion.pack()
    cerrar = Button(reglas, text="Cerrar", command=lambda: reglas.destroy())
    cerrar.pack()

# Creo una ventana de Tkinter
ventana = Tk()
# Preparo las cajas para que puedan recibir valores
caja_titulo = StringVar()
caja_vida_max = StringVar()
caja_historia = StringVar()
# FIXME Crear una caja universal por los nuevos valores dinámicos
# y sobre todo porque las nuevas cajas van a dejar de necesitar el
# método Entry para tener una vista más cómoda al manipular los valores

# Menu Bar
menubar = Menu(ventana)
archivo_menu = Menu(menubar, tearoff=0)
# Añado los botones que van a tener
archivo_menu.add_command(label="Formato Simple", command=lambda: print('Formato basico activado'))
archivo_menu.add_command(label="Formato Datallado", command=lambda: print('Formato pro activado'))
archivo_menu.add_command(label="Guardar", command=lambda: print('Guardando Archivo'))
# TODO Crear un botón para cerrar todas las ventanas que no sean la principal (Quizá con un grup)
# (Opcional) Añadir un botón de Save and exit
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)
# Elijo el nombre del contenedor con los botones
menubar.add_cascade(label="Archivo", menu=archivo_menu)

info_menu = Menu(menubar, tearoff=0)
# Añado los botones que van a tener
info_menu.add_command(label="Reglas", command=ventana_reglas)
info_menu.add_command(label="Ejemplos", command=lambda: print("Mostando ejemplos"))
info_menu.add_command(label="Funcionamiento", command=lambda: print("Mostando funcionamiento"))
# Elijo el nombre del contenedor con los botones
menubar.add_cascade(label="Info", menu=info_menu)

# Label
# (El cuadro de la izquierda)
label_principal = Label(ventana)
label_principal.grid(row=0, column=0, padx=5, pady=3)

# (El cuadro de la derecha)
label_de_ayuda = Label(ventana)
label_de_ayuda.grid(row=0, column=1, padx=5, pady=3)

# Dentro
wrapper0 = LabelFrame(label_principal, text='Carpetitas')
wrapper1 = LabelFrame(label_de_ayuda, text='Visualizador')
wrapper2 = LabelFrame(label_de_ayuda, text='Modificador')

wrapper0.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

img_ch = Image.open("checked.png")
img_un = Image.open("uncheked.png")
# Llamo las imágenes y les ajusto el tamaño
img_checkeado = ImageTk.PhotoImage(img_ch.resize((12, 12)))
img_descheckeado = ImageTk.PhotoImage(img_un.resize((12, 12)))

# Carpetitas
tv = ttk.Treeview(wrapper0)

tv.tag_configure('checked', image=img_checkeado)
# Establezco que cada carpetita con la etiqueta checked se le va a agregar la imagen marcada
# Y cada carpetita con la etiqueta unchecked se le va a agregarla imagen desmarcada
tv.tag_configure('unchecked', image=img_descheckeado)

# Prueba manual de carpetas anidadas con valores
main = tv.insert("", END, text="MAIN", open=1)
tv.insert(main, END, text="TITLE")
tv.insert(main, END, text="MAX_HEALTH")
health_options = tv.insert(main, END, text="HEALTH_OPTIONS")

tv.insert(health_options, END, text="NUMERIC_HEALTH", tags="unchecked", values=[True])
tv.insert(health_options, END, text="PERCENT_HEALTH", tags="unchecked", values=[False])
health_bar = tv.insert(health_options, END, text="HEALTH_BAR")

tv.insert(health_bar, END, text="HEALTH_BAR_DISPLAY", tags="unchecked", values=[True])
tv.insert(health_bar, END, text="LEFT_HEALTH_BAR_SYMBOL")
tv.insert(health_bar, END, text="RIGHT_HEALTH_BAR_SYMBOL")
tv.insert(health_bar, END, text="SIZE_SYMBOL")

tv.insert(health_options, END, text="HEALTH_FORMAT")
states = tv.insert(health_options, END, text="HIDDEN_STATS", tags="unchecked", values=[False])

menu = tv.insert("", END, text="MENU", open=1)
tv.insert(menu, END, text="PLAY", tags="unchecked")
tv.insert(menu, END, text="OPTIONS", tags="unchecked")
tv.insert(menu, END, text="CREDITS", tags="unchecked")
tv.insert(menu, END, text="EXIT", tags="unchecked")

history = tv.insert("", END, text="HISTORY", open=1)
tv.insert(history, END, text="PROLOG", tags="unchecked")
tv.insert(history, END, text="CHAPTERS", tags="unchecked")
tv.pack(side=LEFT)
print(tv.item(history))

# Prueba para cuando tenga que convertir datos de las carpetitas a columnas dinámicas
ejemplo = tv.item(states)['values'][0]
if not ejemplo == '':
    if ejemplo == 'True':
        tv.item(states, tags='checked')
    elif ejemplo == 'False':
        tv.item(states, tags='unchecked')
    elif isinstance(ejemplo, int):
        print('Número')
    elif ejemplo == 'None':
        print('No sé, bro')
print(tv.item(states))

# Visualizador
# Creo una caja con 2 columnas y 5 filas (Temporal)
trv = ttk.Treeview(wrapper1, columns=(1,2), show="headings", height="5")

trv.pack(side=LEFT)
#trv.place(x=0, y=0)
# FIXME Problema con el scroolbar horizontal:
# Al activarlo se arregla pero el height se rompe y viceversa
trv.heading(1, text="Values")
# Nombre de las columnas
trv.heading(2, text="Estructura")
trv.column(1, width=50, minwidth=100)
# Modifico el width para poder hacer scrool horizaontal en las columnas
# (Posiblemente temporal)
trv.column(2, width=150, minwidth=400)

# Con doble click en las columnas llevo la info a las cajas
trv.bind('<Double 1>', getrow)
# Con un click en las carpetas con checkboxes se invierten los estados
tv.bind('<Button 1>', toggleCheck)

# Scrollbal Vertical
visualizador_scrollbar_y = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
visualizador_scrollbar_y.pack(side=RIGHT, fill="y")
carpetitas_scrollbar_y = ttk.Scrollbar(wrapper0, orient="vertical", command=tv.yview)
carpetitas_scrollbar_y.pack(side=RIGHT, fill="y")

# Scrollbal Horizontal
visualizador_scrollbar_x = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
visualizador_scrollbar_x.pack(side=BOTTOM, fill="x")
carpetitas_scrollbar_x = ttk.Scrollbar(wrapper0, orient="horizontal", command=tv.xview)
carpetitas_scrollbar_x.pack(side=BOTTOM, fill="x")

trv.configure(yscrollcommand=visualizador_scrollbar_y, xscrollcommand=visualizador_scrollbar_x)
# TODO Fíjense luego si con visualizador/carpetitas_scrollbar_x/y.set se les ve bien o es error mío
trv.configure(yscrollcommand=carpetitas_scrollbar_y, xscrollcommand=carpetitas_scrollbar_x)

# Actualizo las columnas para que carguen los valores que le añado por defecto
update(prueba)

# Modificador
# Cajas temporales para ingresar texto
eTitulo = Label(wrapper2, text="Titulo: ")
eTitulo.grid(row=0, column=0, padx=5, pady=3)

# TODO Usar solo Entry para valores numéricos, de lo contrario reemplacémoslo por
# Text para el uso de múltiples líneas
# PD: Tenemos que elegir un tipo de fuente amigable, la de por defecto llama la atención
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

##########
"""
# Prueba del sistema automático de jerarquía de carpetas (En progreso)
# PD: Luego si quieren les explico, de todos modos aun no está terminado, por eso se ve horrible

# import json
# with open('C:\\Users\\Lucas\\Desktop\\Se me va la cabeza\\Clases Python\\Desafio\\Libreta-de-direcciones-IP\\Juego Nahu\\EscenariosPrincipales.json', 'r', encoding='utf8') as archivo:
#     datos = json.load(archivo)
#     print(list(datos["MENU"].items())[0])

si = {'MAIN': {'TITLE': 'Return: Mi travesía de volver a casa', 'MAX_HEALTH': 100, 'HEALTH_OPTIONS': {'NUMERIC_HEALTH': True, 'PERCENT_HEALTH': False, 'HEALTH_BAR': {'HEALTH_BAR_DISPLAY': True, 'LEFT_HEALTH_BAR_SYMBOL': '#', 'RIGHT_HEALTH_BAR_SYMBOL': '-', 'SIZE_SYMBOL': 20}, 'HEALTH_FORMAT': '{HEALTH_BAR}  {NUMERIC_HEALTH}', 'HIDDEN_STATS': False}}, 'MENU': {'PLAY': 'Jugar', 'OPTIONS': {'NAME': 'Opciones', 'DETAILS': {'VOLUME': 'Volumen', 'TEXT_SIZE': 16}}, 'CREDITS': 'Le agradezco a Python por dejarme programarle', 'EXIT': 'Salir'}, 'HISTORY': {'PROLOG': 'Una noche cualquiera, nuestro personaje se va a dormir, y luego de dormir, el siente que se despierta, pero se despierta en una realidad totalmente diferente, al ir a su armario, se encuentra con prendas de un origen desconocido y medianamente antiguas, las cuales se termina por poner, luego de salir de su hogar, se encuentra en un mundo distinto, en una aldea remota, luego de salir de esa aldea, nuestro personaje se pierde en un bosque, y a partir de ahí, comienza su aventura para poder volver a su mundo real\n¿Logrará hacerlo?', 'CHAPTERS': [{'CHAPTER_NAME': 'El bosque de las almas perdidas', 'INITIAL_HEALTH': {'SET_HEALTH': True, 'NEW_HEALTH': 100}, 'STORYTELLER': None, 'INTERNAL_VOICE': 'Acabo de perderme en este bosque, lo único que escucho mas alla de mis propios pasos son\ngritos de almas, desesperadas por volver a la vida, parece que estan sufriendo una horrible\n pesadilla sin poder descansar en paz\n\nMuchas de estas palabras, estan en idiomas que desconozco, ni siquiera estan hablando en\nEspañol o Ingles, podría llegar a decir que estas estan en un idioma tan antiguo como este\nlugar', 'PROTAGONIST_DIALOGUE': None, 'OPTIONAL_TEXT': "(Encontraste una nota, 'El sucumbir de las almas desesperadas')", 'PROTAGONIST_STATS': {'DAMAGE': None, 'HEALING': None, 'POISON': None, 'BLEED_OUT': None}}]}}

prueba = {'MAIN': 'Hola', 'MENU': '¿Qué tal?','HISTORY': {'Bien': 'si', "coso": [{"cosito": 'de cosoy'}, {"cosito2": 'de cosoy'}]}}

ventana = Tk()
tv = ttk.Treeview(ventana)

tv.insert("", END, "MAIN", text="MAIN", open=1)
tv.insert("", END, "MENU", text="MENU", open=1)
tv.insert("", END, "HISTORY", text="HISTORY", open=1)

def enrutador_principal(lista, buscar):
    def enrutador(estilo, valor):
        if estilo == valor:
            return [estilo]
        elif isinstance(estilo, dict):
            for k, v in estilo.items():
                p = enrutador(v, valor)
                if p:
                    return [k] + p
        elif isinstance(estilo, list):
            lst = estilo
            for i in range(len(lst)):
                p = enrutador(lst[i], valor)
                if p:
                    return [str(i)] + p
    try:
        return '/'.join(enrutador(lista, buscar)[:-1])
    except:
        return enrutador(lista, buscar)
# Paro
ruta = []
ruta2 = []
candado = [False]
indexacion = []

def enrutador2(cadena=''):
    if not candado[0]:
        ruta2.extend(ruta)
    else:
        pass
    #print(ruta2)
    if not len(indexacion) == 0:
        for i in indexacion:
            if ruta[-1] == i[2]:
                ruta.pop()
                ruta.extend(i)
                print(ruta[-3:])
                # indexacion.clear()
    print(ruta)
    if len(cadena.split('/')) > 2:
        print(cadena.split('/')[-3:])
    # ruta2.clear()
    # ruta2.extend(ruta)
    # print(ruta2)

print(
    '/'.join(['Hola', "Maria"])
)

def crear_arbolito(arbolito):
    for i in list(arbolito.items()):
        if isinstance(i[1], (dict)):
            for q in i[1].items():
                tv.insert(i[0], END, q[0], text=q[0])
            ruta.append(i[0])
            crear_arbolito(i[1])
        
        elif isinstance(i[1], (list)):
            candado.clear()
            candado.append(True)
            ruta2.append(len(i[1])-1)
            for idx in range(len(i[1])):
                tv.insert(i[0], END, f'[{idx}]', text=f'[{idx}]')
                for exacto in list(i[1][idx].items()):
                    coso = tv.insert(f'[{idx}]', END, exacto[0], text=exacto[0])
                    indexacion.append([i[0], tv.parent(coso)[1], tv.item(coso)["text"]])
            for dentro in i[1]:
                crear_arbolito(dentro)
        else:
            ruta.append(i[0])
            if not candado[0]:
                ruta2.clear()
            enrutador2()
            ruta.pop()
            # enrutador2()
            enrutador2(enrutador_principal(prueba, i[1]))
            print('\n')
            # ruta2.append(i[0])
            try:
                if isinstance(i[1], bool):
                    tv.insert(i[0], END, text=str(i[1]))
                else:
                    tv.insert(i[0], END, text=i[1])
            except:
                tv.insert(i[0], END, text=str(i[1]))

crear_arbolito(prueba)

tv.pack()

ventana.title("Editor Histórico")
ventana.geometry('750x350')

ventana.mainloop()
"""