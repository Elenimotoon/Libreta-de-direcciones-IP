from os import system

class Escenario:
    def __init__(self, descripcion, opciones):
        self.descripcion = descripcion
        self.opciones = opciones
        self.cambiosSalud = 0
    
    def presentar(self, personaje):
        print('\n')
        print(personaje.SaludPersonaje())
        print(self.descripcion)
        
        personaje.salud += self.cambiosSalud
        
        if personaje.salud <= 0:
            new_game = True
            
            while new_game:
                eleccion = input("La haz palmado, tío...\n\n¿Quieres intentarlo otra vez?\ny/n\n")
                match eleccion:
                    case "n":
                        raise SystemExit(0)
                    case "y":
                        system("CLS")
                        new_game = False
                    case _:
                        print('¡Selección invalida! Vuelve a intentarlo.')
            
            personaje.salud = 0
            return 'INICIO'
        
        for i in range(len(self.opciones)):
            print(f"[{i}] {self.opciones[i].descripcion}")
        
        error = True
        
        while error:
            eleccion = input()
            
            if eleccion.isnumeric():
                eleccion = int(eleccion)
                
                if eleccion < len(self.opciones):
                    error = False
            
            if error:
                print('¡Selección invalida! Vuelve a intentarlo.')
            
            if not error:
                return self.opciones[eleccion].siguienteFragmento