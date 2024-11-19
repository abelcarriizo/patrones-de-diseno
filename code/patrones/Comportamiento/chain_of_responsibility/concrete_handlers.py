from handler_base import Manejador_Base

class Asistente(Manejador_Base):
  def manejar(self, solicitud):
    if solicitud == 'solicitud sencilla':
      return f'La solicitud fue manejada por el Asistente'
    return super().manejar(solicitud)
  
class Director(Manejador_Base):
  def manejar(self, solicitud):
    if solicitud == 'solicitud normal':
      return f'La solicitud fue manejada por el Director'
    return super().manejar(solicitud)

class Jefe(Manejador_Base):
  def manejar(self, solicitud):
    if solicitud == 'solicitud dificil':
      return f'La solicitud fue manejada por el Jefe'
    return super().manejar(solicitud)
