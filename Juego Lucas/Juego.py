from Opcion import Opcion
from Escenario import Escenario
from Personaje import Personaje
# Llamo las partes del juego para que funcione toda la lógica

personaje = Personaje()
escenarioActual = None
final = False
escenarios = {}
# Establezco opciones por defecto que luego voy a ir actualizando

with open('EscenariosPrincipales.txt', 'r', encoding='utf8') as archivo:
    # Llamo a la historia para leerla con el tipo de letras especiales, 
    # coloco el cursor al principio y almaceno la lectura del archivo
    archivo.seek(0)
    contenido = archivo.read()
    
    # Divido las acciones principales (Narración, Acciones, Vida) en secciones
    partes = contenido.split("#")
    
    for p in range(len(partes)):
        
        if len(partes[p]) > 0:
            
            escenario = partes[p].split("*")
            # Separo narración de acciones
            partesEscenario = escenario[0].split("|")
            
            opciones = []
            
            for e in range(len(escenario)):
                if e > 0:
                    # Separo la clave de las acciones de las acciones en si
                    partesOpcion = escenario[e].split("|")
                    # Le mando a Opcion las acciones y luego su identificador
                    o = Opcion(partesOpcion[1].rstrip(), partesOpcion[0])
                    opciones.append(o)
            
            # Le mando la información a Escenario y espero a que se elija una opción antes de seguir
            e = Escenario(partesEscenario[1], opciones)
            
            if 2 < len(partesEscenario):
                # # Verifico si se ha establecido un cambio de salud y luego lo modifico
                e.cambiosSalud = int(partesEscenario[2])
            escenarios[partesEscenario[0]] = e

escenarioActual = escenarios['INICIO']
# Establezco INICIO por defecto por si un Game Over que se vuelva a reiniciar desde ese punto

while not final:
    # Si aun no se ha muerto el personaje entonces pasará al siguiente capitulo
    siguiente = escenarioActual.presentar(personaje)
    escenarioActual = escenarios[siguiente]