from code import Singleton

singleton_1 = Singleton()
singleton_2 = Singleton()

# Comprobar si s1 y s2 son la misma instancia
print(f"singleton_1 es singleton_2: {singleton_1 is singleton_2}")  # Debería imprimir True
print(f"ID de s1: {id(singleton_1)}")
print(f"ID de s2: {id(singleton_2)}")