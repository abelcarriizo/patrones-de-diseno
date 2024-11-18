class ConversorMoneda:
    def __init__(self):
        self.tasa_dolar_a_peso = 350

    def dolar_a_peso(self, dolares):
        return dolares * self.tasa_dolar_a_peso

    def peso_a_dolar(self, pesos):
        return pesos / self.tasa_dolar_a_peso

if __name__ == '__main__':
    conversor = ConversorMoneda()
    
    dolares = 100
    pesos = conversor.dolar_a_peso(dolares)
    print(f'{dolares} dólares son {pesos} pesos argentinos.')
    
    pesos = 35000
    dolares = conversor.peso_a_dolar(pesos)
    print(f'{pesos} pesos argentinos son {dolares} dólares.')