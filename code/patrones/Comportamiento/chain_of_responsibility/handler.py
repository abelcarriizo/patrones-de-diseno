from abc import ABC, abstractmethod

class Manejador(ABC):
  def __init__(self) -> None:
    self.siguiente_manejador = None

  def establecer_siguiente(self, manejador):
    self.siguiente_manejador = manejador
    return manejador # Permite encadenar manejadores
  
  @abstractmethod
  def manejar(self):
    pass
