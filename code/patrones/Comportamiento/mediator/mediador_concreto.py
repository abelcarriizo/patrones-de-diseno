from mediador import Mediador

class Mediador_Concreto(Mediador):
  def __init__(self, boton, luz):
    self.boton = boton
    self.luz = luz
    self.boton.establecer_mediador(self)
    self.luz.establecer_mediador(self)

  def notificar(self, emisor, evento):
    if emisor == self.boton and evento == 'click':
      if self.luz.encendida:
        self.apagar()
      else:
        self.luz.apagar()