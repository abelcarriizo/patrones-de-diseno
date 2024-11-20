from boton import Boton
from luz import Luz
from mediador_concreto import Mediador_Concreto

if __name__ == "__main__":
    # Crear los componentes
    boton = Boton()
    luz = Luz()

    # Crear el mediador
    mediador = Mediador_Concreto(boton, luz)

    # Simular interacciones
    boton.click(mediador)  # La luz se enciende
    boton.click(mediador)  # La luz se apaga