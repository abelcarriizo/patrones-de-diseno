from builder import ComputadoraBuilder

class Director:
  def __init__(self, builder:ComputadoraBuilder):
    self.builder = builder

  def construccion_completa(self):
    self.builder.construir_cpu()
    self.builder.construir_gpu()
    self.builder.construir_ram()

  def mostrar_computadora(self):
    return self.builder.mostrar_resultados()