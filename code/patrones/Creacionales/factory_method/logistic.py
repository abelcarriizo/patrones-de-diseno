from abc import ABC, abstractmethod

#creator
class Logistic:
  @abstractmethod
  def factoryMethod(self):
    pass

  def someOperation(self):
    product = self.factoryMethod()
    result = f'Mi product = {product}'
    return result

#concrete creator 1
class RoadLogistcs(Logistic):
  def factoryMethod(self):
    return Truck()

#concrete creator 2
class SeaLogistics(Logistic):
  def factoryMethod(self):
    return Ship()


#product / interface
class Transport(ABC):
  @abstractmethod
  def deliver(self):
    pass

#concrete product 1
class Truck(Transport):
  def deliver(self):
    return 'Transport: Truck'

#concrete product 2 
class Ship(Transport):
  def deliver(self):
    return 'Transport: Ship'


if __name__=='__main__':
  road = RoadLogistcs()
  print(road.someOperation())