import io

from Opcion import Opcion
from Escenario import Escenario
from Jugador import Jugador

jugador = Jugador()
escenarioActual = None
final = False
escenarios = {}

with io.open('EscenariosPrincipales.txt', 'r', encoding='utf8') as archivo:
    archivo.seek(0)
    contenido = archivo.read()

escenarioActual = escenarios['INICIO']

while not final:
    siguiente = escenarioActual.presentar(jugador)
    escenarioActual = escenarios[siguiente]