from os import system

class Escenario:
    def __init__ (self, opciones, descripcion):
        self.opciones = opciones
        self.descripcion = descripcion
        self.cambiosSalud = 0
    
    def presentar(self, personaje):
        
        personaje.salud += self.cambiosSalud
        
        print(f'\n{personaje.SaludPersonaje()}\n{self.descripcion}')
        
        if personaje.salud <= 0:
            new_game = True
            
            while new_game:
                eleccion_letras = input("Moriste\n\nAgain?\ny/n\n")
                match eleccion_letras.upper():
                    case "N" | "NO":
                        raise SystemExit(0)
                    case "Y" | "YES" | "S" | "SI" | "SÍ":
                        system("clear")
                        new_game = False
                    case _:
                        print('Selecciona la opción correcta.')
            
            personaje.salud = 100
            return 'INICIO'
        
        for i in range(len(self.opciones)):
            print(f"[{i}] {self.opciones[i].descripcion}")
        
        error = True
        repeticion = False
        
        while error:
            eleccion_numero = input()
            
            if eleccion_numero.isnumeric():
                eleccion_numero = int(eleccion_numero)
                
                if eleccion_numero < len(self.opciones):
                    error = False
            
            if error:
                repeticion = True
                print('Selecciona la opción correcta.')
            
            if not error:
                if repeticion:
                    system("clear")
                system("clear -x")
                return self.opciones[eleccion_numero].siguienteFragmento

"""
#Pruebas, solo ignorar
from time import sleep
cap1 = "Acabo de perderme en este bosque, lo único que escucho mas alla de mis propios pasos son gritos de almas, desesperadas por volver a la vida, parece que estan sufriendo una horrible pesadilla sin poder descansar en paz"

for letra in cap1:
    print(letra, end="")
    sleep(0.05)

#Transformación de str a json
#Ya no es necesaria, voy a cambiar el formato .txt por .json
import json
titulo = '{"TITLE": "Mi travesía de volver a casa"}'
print(json.loads(titulo)["TITLE"])
"""