from abc import ABC, abstractmethod

class Laptop(ABC):
  def marca(self):
    pass

  def bateria(self):
    pass

class Apple(Laptop):
  def __init__(self, modelo, bateria) -> None:
    self.modelo = modelo
    self.bateria = bateria

  def obtener_modelo(self):
    print(f'Laptop: Mac {self.modelo}')

  def obtener_bateria(self):
    print(f'Bateria: {self.bateria}')

class Samsung(Laptop):
  def __init__(self, modelo, bateria) -> None:
    self.modelo = modelo
    self.bateria = bateria

  def obtener_modelo(self):
    print(f'Laptop: Samsung {self.modelo}')

  def obtener_bateria(self):
    print(f'Bateria: {self.bateria}')