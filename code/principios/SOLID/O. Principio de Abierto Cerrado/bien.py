tasas_cambio = {
    "USD_ARS": 20,    # 1 dólar equivale a 20 pesos
    "ARS_USD": 0.05,  # 1 peso equivale a 0.05 dólares
}

class Conversor():
  def __init__(self, tasa_moneda):
    self.tasas_cambio = tasa_moneda

  def convertir(self, cantidad, moneda_origen, moneda_destino):
    clave = f"{moneda_origen}_{moneda_destino}"
    tasa = self.tasas_cambio.get(clave)
    if tasa is None:
      raise ValueError(f"No existe una tasa de cambio para {clave}")
    return cantidad * tasa

if __name__=='__main__':
  conversor = Conversor(tasas_cambio)
  cantidad_en_peso = conversor.convertir(20, 'USD', 'ARS') # dolar a peso
  print(f'20 USD son: "{cantidad_en_peso}ARS"')