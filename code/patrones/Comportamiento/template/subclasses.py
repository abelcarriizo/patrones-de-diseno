from template import Beverage

# Subclase para preparar café
class Coffee(Beverage):
    def add_main_ingredient(self):
        print("Agregando café molido.")

# Subclase para preparar té
class Tea(Beverage):
    def add_main_ingredient(self):
        print("Agregando hojas de té.")
