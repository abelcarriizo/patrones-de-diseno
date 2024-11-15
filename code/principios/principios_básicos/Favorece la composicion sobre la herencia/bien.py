class Motor:
  def encender(self):
    print('Motor encendido')
  
class Radio:
  def encender(self):
    print('Radio encendida')

class Auto:
  def __init__(self):
    self.motor = Motor()
    self.radio = Radio()
  
  def encender(self):
    self.motor.encender()
    self.radio.encender()

if __name__=='__main__':
  auto = Auto()
  auto.encender()