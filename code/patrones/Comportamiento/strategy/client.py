from strategy_concrete import *
from context import DiscountContext

if __name__ == "__main__":
    # Crear estrategias concretas
    regular_discount = RegularDiscount()
    vip_discount = VIPDiscount()
    no_discount = NoDiscount()

    # Crear el contexto con una estrategia inicial
    context = DiscountContext(regular_discount)

    # Calcular descuentos para diferentes estrategias
    amount = 100.0  # Precio base

    print(f"Regular Discount: {context.calculate_discount(amount)}")  # 90.0

    # Cambiar a estrategia VIP
    context.set_strategy(vip_discount)
    print(f"VIP Discount: {context.calculate_discount(amount)}")  # 80.0

    # Cambiar a estrategia sin descuento
    context.set_strategy(no_discount)
    print(f"No Discount: {context.calculate_discount(amount)}")  # 100.0
