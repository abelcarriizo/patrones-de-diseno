from builder import ComputadoraBuilder
from product import Computadora

class ComputadoraGamer(ComputadoraBuilder):
  def __init__(self) -> None:
    self.reset()

  def reset(self):
    self.computadora = Computadora()

  def construir_cpu(self):
    self.computadora.agregar_componentes('CPU', 'Intel Core I9')
  
  def construir_gpu(self):
    self.computadora.agregar_componentes('GPU', 'NVIDIA RTX 4090')

  def construir_ram(self):
    self.computadora.agregar_componentes('RAM', '32gb DDR5 5200mhz')

  def mostrar_resultados(self):
    producto = self.computadora.mostrar_computadora()
    self.reset()
    return producto
  
class ComputadoraOficina(ComputadoraBuilder):
  def __init__(self) -> None:
    self.reset()

  def reset(self):
    self.computadora = Computadora()

  def construir_cpu(self):
    self.computadora.agregar_componentes('CPU', 'Intel Core I5')
  
  def construir_gpu(self):
    self.computadora.agregar_componentes('GPU', 'Intel Xiris')

  def construir_ram(self):
    self.computadora.agregar_componentes('RAM', '8gb DDR5 4200mhz')

  def mostrar_resultados(self):
    producto = self.computadora.mostrar_computadora()
    self.reset()
    return producto