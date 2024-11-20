from abc import ABC, abstractmethod

class Mediador(ABC):
  @abstractmethod
  def notificar(self):
    pass