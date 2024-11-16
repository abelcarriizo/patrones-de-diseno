class Calculadora:
  def calcular(self, a:int, b:int, operacion:str):
    if operacion == 'sumar':
      return a + b
    elif operacion == 'restar':
      return a - b
