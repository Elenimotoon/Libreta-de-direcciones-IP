class Escenario:
    def __init__(self , descripcion , opciones):
        self.descripcion = descripcion
        self.opciones = opciones
        self.cambiosSupervivencia = 0
    
    def presentar(self, personaje):
        print('\n')
        print(personaje.obtenerEstado())
        print(self.descripcion)
        
        personaje.supervivencia += self.cambiosSupervivencia
        
        if personaje.supervivencia <= 0:
            print("La haz palmado, tío...\n\n¿Quieres intentarlo otra vez?")
            personaje.supervivencia = 0
            return 'INICIO'
        
        for i in range(len(self.opciones)):
            print("[" + str(i) + "] " + self.opciones[i].descripcion)
        
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