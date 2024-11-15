class MetodoPago:
  def procesarPago(self, monto:float):
    raise NotImplementedError("Este método debe ser implementado por subclases.")
  
class Tarjeta(MetodoPago):
  def procesarPago(self, monto:float):
    print(f'Procesando pago con tarjeta: {monto}')

class Efectivo(MetodoPago):
  def procesarPago(self, monto:float):
    print(f'Procesando pago con tarjeta: {monto}')

def procesadorPago(metodo:MetodoPago, monto:float):
  metodo.procesarPago(monto)

if __name__=='__main__':
  tarjeta = Tarjeta()
  procesadorPago(tarjeta, 10)