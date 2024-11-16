from abc import ABC, abstractmethod

class Operacion(ABC):
  @abstractmethod
  def calcular(self, a, b):
    pass

class Sumar(Operacion):
  def calcular(self, a, b):
    return a + b
  
class Restar(Operacion):
  def calcular(self, a, b):
    return a - b
  
class Calculadora:
  def calcular(self, a, b, operacion:Operacion):
    return operacion.calcular(a, b)
