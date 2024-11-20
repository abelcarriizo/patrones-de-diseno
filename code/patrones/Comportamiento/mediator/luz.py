from componente_base import Componente_Base

class Luz(Componente_Base):
    def __init__(self):
        self.encendida = False

    def encender(self):
        self.encendida = True
        print("La luz está ENCENDIDA.")

    def apagar(self):
        self.encendida = False
        print("La luz está APAGADA.")