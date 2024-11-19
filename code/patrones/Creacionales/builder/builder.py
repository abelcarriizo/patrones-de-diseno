from abc import ABC, abstractmethod

class ComputadoraBuilder(ABC):
  @abstractmethod
  def reset(self):
    pass

  @abstractmethod
  def construir_cpu(self):
    pass

  @abstractmethod
  def construir_gpu(self):
    pass

  @abstractmethod
  def construir_ram(self):
    pass

  @abstractmethod
  def mostrar_resultados(self):
    pass
