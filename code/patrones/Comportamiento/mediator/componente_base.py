class Componente_Base:
  def __init__(self):
    self.mediador = None

  def establecer_mediador(self, mediador):
    self.mediador = mediador