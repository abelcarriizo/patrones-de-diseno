from abc import ABC, abstractmethod

class Celular(ABC):
  def marca(self):
    pass

  def bateria(self):
    pass

class Apple(Celular):
  def __init__(self, modelo, bateria) -> None:
    self.modelo = modelo
    self.bateria = bateria

  def obtener_modelo(self):
    print(f'Celular: Iphone {self.modelo}')

  def obtener_bateria(self):
    print(f'Bateria: {self.bateria}')

class Samsung(Celular):
  def __init__(self, modelo, bateria) -> None:
    self.modelo = modelo
    self.bateria = bateria

  def obtener_modelo(self):
    print(f'Celular: Samsung {self.modelo}')

  def obtener_bateria(self):
    print(f'Bateria: {self.bateria}')