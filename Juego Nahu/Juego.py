import json
from Opcion import Opcion
from Escenario import Escenario
from Jugador import Jugador
# Llamo las partes del juego para que funcione toda la lógica

jugador = Jugador()
escenarioActual = None
final = False
escenarios = {}
# Establezco opciones por defecto que luego voy a ir actualizando

with open('EscenariosPrincipales.json', 'r', encoding='utf8') as archivo:
    # Llamo al JSON para leerlo con el tipo de letras especiales y
    # lo convierto en un diccionario de Python
    contenido = json.load(archivo)

"""
escenarioActual = escenarios['INICIO']

while not final:
    siguiente = escenarioActual.presentar(jugador)
    escenarioActual = escenarios[siguiente]
"""