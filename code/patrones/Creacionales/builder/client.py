from director import Director
from concrete_builder import ComputadoraGamer

if __name__=='__main__':
  pc_gamer = ComputadoraGamer()
  director = Director(pc_gamer)
  director.construccion_completa()
  director.mostrar_computadora()