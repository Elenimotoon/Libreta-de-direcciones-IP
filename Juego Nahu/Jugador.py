import json
import re

with open('EscenariosPrincipales.json', 'r') as archivo:
    # Creo un diccionario a partir del texto JSON
    datos = json.load(archivo)
    
    class Jugador:
        def __init__(self):
            # Guardo la salud inicial
            vida_inicial = datos["HISTORY"]["CHAPTERS"][0]["INITIAL_HEALTH"]
            # Compruebo que vida_inicial no esté vacía, que tenga la opción para establecer nombres
            # y que esté activa, de lo contrario no se permitirá iniciar el juego
            if len(vida_inicial) == 0 and not "SET_HEALTH" in vida_inicial and not vida_inicial["SET_HEALTH"]:
                self.salud = 0
                return
            # Establezco la salud inicial a la elegida en el capitulo 1
            self.salud = vida_inicial["NEW_HEALTH"]
            
        def SaludPersonaje(self):
            # Guardo el objeto con las opciones establecidas
            opciones_de_vida = datos["MAIN"]["HEALTH_OPTIONS"]
            salud_maxima = datos["MAIN"]["MAX_HEALTH"]
            cantidad_de_simbolos = opciones_de_vida["HEALTH_BAR"]["SIZE_SYMBOL"]
            simbolo_izquierdo = opciones_de_vida["HEALTH_BAR"]["LEFT_HEALTH_BAR_SYMBOL"]
            simbolo_derecho = opciones_de_vida["HEALTH_BAR"]["RIGHT_HEALTH_BAR_SYMBOL"]
            
            # Creo por defecto acciones vacías antes de comprobar que existen
            NUMERIC_HEALTH = ''
            PERCENT_HEALTH = ''
            HEALTH_BAR = ''
            PROTAGONIST_STATS = ''
            
            formato_de_salud = opciones_de_vida["HEALTH_FORMAT"]
            # Utilizo una expresión regular para transformar los datos entre llaves {} a valores
            filtro = re.findall(r'\{([^}]+)\}', formato_de_salud)
            barra_de_vida = opciones_de_vida["HEALTH_BAR"] and opciones_de_vida["HEALTH_BAR"]["HEALTH_BAR_DISPLAY"]
            
            def obtener_barra_de_vida(salud):
                # Obtengo la cantidad de símbolos posibles dentro del máximo de vida
                simbolos_convertidos = int(salud_maxima/cantidad_de_simbolos)
                # Obtengo la cantidad de símbolos que pueden ir dentro de la salud
                simbolos_actuales = int(salud/simbolos_convertidos)
                salud_restante = cantidad_de_simbolos - simbolos_actuales
                
                vida_actual = simbolo_izquierdo * simbolos_actuales
                vida_restante = simbolo_derecho * salud_restante
                
                return f"|{vida_actual}{vida_restante}|"
            
            if opciones_de_vida["NUMERIC_HEALTH"]:
                NUMERIC_HEALTH = self.salud
            
            if opciones_de_vida["PERCENT_HEALTH"]:
                PERCENT_HEALTH = f'{int((self.salud/salud_maxima) * 100)}%'
            
            if barra_de_vida:
                HEALTH_BAR = obtener_barra_de_vida(self.salud)
            
            if opciones_de_vida["HIDDEN_STATS"]:
                # Si el personaje está bien en algún sentido de salud entonces
                # se va ocultar solo donde esté bien
                if NUMERIC_HEALTH == salud_maxima:
                    NUMERIC_HEALTH = ''
                if PERCENT_HEALTH == '100%':
                    PERCENT_HEALTH = ''
                if barra_de_vida and HEALTH_BAR == obtener_barra_de_vida(salud_maxima):
                    HEALTH_BAR = ''
            
            for s in filtro:
                # Reemplazo el string entre llaves por el valor al que mencionan
                formato_de_salud = re.sub('{'+s+'}', str(eval(s)), formato_de_salud)
            
            return formato_de_salud
"""
Prueba
input(Jugador().SaludPersonaje())
"""