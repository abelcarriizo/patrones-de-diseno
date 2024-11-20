from temperatura_converter import TemperaturaConverter
from fahrenheit_service import Fahrenheit_to_Celsius

class Fahrenheit_to_Celsius_Adapter(TemperaturaConverter):
  def __init__(self, service:Fahrenheit_to_Celsius):
    self.service = service
  
  def convert(self, fahrenheit:float):
    return self.service.fahrenheit_to_celsius(fahrenheit)