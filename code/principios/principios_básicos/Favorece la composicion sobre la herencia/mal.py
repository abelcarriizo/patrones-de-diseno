class Vehiculo:
  def encender(self):
    print('Vehiculo encendido')

class Auto(Vehiculo):
  def tocarBocina(self):
    print('*Sonido de bocina*')

class Camion(Vehiculo):
  def cargar(self):
    print('*Cargando camion...*')

if __name__=='__main__':
  print('A U T O')
  auto = Auto()
  auto.encender()
  auto.tocarBocina()

  print('')

  print('C A M I O N')
  camion = Camion()
  camion.encender()
  camion.cargar()