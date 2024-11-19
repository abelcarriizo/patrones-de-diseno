from concrete_handlers import *

if __name__=='__main__':
  asistente = Asistente()
  director = Director()
  jefe = Jefe()

  asistente.establecer_siguiente(director).establecer_siguiente(jefe)

  solicitudes = ['solicitud sencilla', 'solicitud normal', 'solicitud dificil', 'solicitud desconocida']

  for solicitud in solicitudes:
    resultado = asistente.manejar(solicitud)
    print(f"Solicitud: '{solicitud}' -> {resultado}")