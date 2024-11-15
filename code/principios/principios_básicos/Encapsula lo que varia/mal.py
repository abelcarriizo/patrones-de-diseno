class MetodoPago:
  def procesarPago(self, metodo:str, monto:float):
    if metodo == 'Tarjeta':
      print(f'Procesando pago con {metodo}: {monto}')
    elif metodo == 'Efectivo':
      print(f'Procesando pagon con {metodo}: {monto}')
    else:
      print(f'Procesando pagon con {metodo}: {monto}')

if __name__=='__main__':
  tarjeta = MetodoPago()
  tarjeta.procesarPago('Tarjeta', 100)