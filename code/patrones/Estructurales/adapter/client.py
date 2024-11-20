from fahrenheit_service import Fahrenheit_to_Celsius
from adapter import Fahrenheit_to_Celsius_Adapter

if __name__=='__main__':
  service = Fahrenheit_to_Celsius()
  adapter = Fahrenheit_to_Celsius_Adapter(service)
  
  fahrenheit = 100
  celsius = adapter.convert(fahrenheit)

  print(f'{fahrenheit}F es igual a {celsius}°C')