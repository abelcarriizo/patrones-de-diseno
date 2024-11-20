from componente_base import Componente_Base

class Boton(Componente_Base):  
  def click(self, mediador):
    print('Boton presionado!')
    mediador.notificar(self, 'click')
    