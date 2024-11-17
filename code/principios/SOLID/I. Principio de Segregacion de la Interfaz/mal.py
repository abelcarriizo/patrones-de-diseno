from abc import ABC, abstractmethod

class CloudProvider(ABC):
  @abstractmethod
  def storeFile(self, name):
    pass

  @abstractmethod
  def getFile(self, name):
    pass

  @abstractmethod
  def createServer(self, region):
    pass

  @abstractmethod
  def listServers(self, region):
    pass

class Amazon(CloudProvider):
  def storeFile(self, name):
    print(f'Almacenando archivo: {name}')

  def getFile(self, name):
    print(f'Archivo obtenido: {name}')

  def createServer(self, region):
    print(f'Servidor creado en: {region}')

  def listServers(self, region):
    print(f'Lista de servidores en la region: {region}...')

class Achicoria(CloudProvider):
  def storeFile(self, name):
    print(f'Almacenando archivo: {name}')

  def getFile(self, name):
    print(f'Archivo obtenido: {name}')
  