from abc import ABC, abstractmethod

from celulares import Apple as celular_apple
from celulares import Samsung as celular_samsung
from laptops import Apple as laptop_apple
from laptops import Samsung as laptop_samsung

class Factory(ABC):
  def crear_celular(self):
    pass

  def crear_laptop(self):
    pass

class Apple(Factory):  
  def crear_celular(self, modelo, bateria):
    celular = celular_apple(modelo, bateria)
    return celular.obtener_modelo()

  def crear_laptop(self,modelo, bateria):
    laptop = laptop_apple(modelo, bateria)
    return laptop.obtener_modelo()  

class Samsung(Factory):  
  def crear_celular(self, modelo, bateria):
    celular = celular_samsung(modelo, bateria)
    return celular.obtener_modelo()

  def crear_laptop(self,modelo, bateria):
    laptop = laptop_samsung(modelo, bateria)
    return laptop.obtener_modelo()


if __name__=='__main__':
  apple_factory = Apple()
  apple_factory.crear_celular('Iphone 15 Pro', '4000 mA')
  apple_factory.crear_laptop('M1 Pro', '15000mA')

  samsung_factory = Samsung()
  samsung_factory.crear_celular('S24 Ultra', '4000mA')
  samsung_factory.crear_laptop('Galaxy Book', '15000mA')

  
