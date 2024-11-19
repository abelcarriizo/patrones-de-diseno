class Computadora:
  def __init__(self) -> None:
    self.componentes = dict()

  def agregar_componentes(self, tipo, marca):
    self.componentes[tipo] = marca

  def mostrar_computadora(self):
    print(self.componentes)