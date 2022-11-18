from os import system

pre_guardado = []

class Escenario:
    def __init__(self, descripcion, opciones):
        self.descripcion = descripcion
        self.opciones = opciones
        self.cambiosSalud = 0
    
    def presentar(self, personaje):
        
        personaje.salud += self.cambiosSalud
        
        decisiones = f'\n{personaje.SaludPersonaje()}\n{self.descripcion}'
        pre_guardado.append(decisiones)
        print(decisiones)
        
        if personaje.salud <= 0:
            new_game = True
            
            while new_game:
                eleccion_letras = input("La haz palmado, tío...\n\n¿Quieres intentarlo otra vez?\ny/n\n")
                match eleccion_letras.upper():
                    case "N" | "NO":
                        raise SystemExit(0)
                    case "Y" | "YES" | "S" | "SI" | "SÍ":
                        system("clear")
                        del pre_guardado[:]
                        new_game = False
                    case _:
                        print('¡Selección invalida! Vuelve a intentarlo.')
            
            personaje.salud = 100
            return 'INICIO'
        
        for i in range(len(self.opciones)):
            elecciones = f"[{i}] {self.opciones[i].descripcion}"
            pre_guardado.append(elecciones)
            print(elecciones)
        
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
                print('¡Selección invalida! Vuelve a intentarlo.')
            
            if not error:
                if repeticion:
                    system("clear")
                    print("\n".join(pre_guardado))
                system("clear -x")
                return self.opciones[eleccion_numero].siguienteFragmento