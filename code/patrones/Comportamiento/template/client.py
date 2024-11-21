from subclasses import *

if __name__ == "__main__":
    # Preparar café
    print("Preparando café:")
    coffee = Coffee()
    coffee.prepare_beverage()

    print("\nPreparando té:")
    # Preparar té
    tea = Tea()
    tea.prepare_beverage()
