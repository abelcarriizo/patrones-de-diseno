from handler import Manejador

class Manejador_Base(Manejador):
  def manejar(self, solicitud):
    if self.siguiente_manejador:
      return self.siguiente_manejador.manejar(solicitud)
    return f'Nadie logro maneja la solicitud {solicitud}'