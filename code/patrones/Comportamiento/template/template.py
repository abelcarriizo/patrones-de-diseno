from abc import ABC, abstractmethod

# Clase base (Template)
class Beverage(ABC):
    # Método plantilla que define los pasos
    def prepare_beverage(self):
        self.boil_water()
        self.add_main_ingredient()
        self.serve()

    # Método concreto
    def boil_water(self):
        print("Hirviendo agua...")

    # Método abstracto (subclases deben implementarlo)
    @abstractmethod
    def add_main_ingredient(self):
        pass

    # Método concreto
    def serve(self):
        print("Sirviendo la bebida caliente.")
