from strategy import DiscountStrategy

# Estrategia: Descuento normal
class RegularDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.90  # 10% de descuento

# Estrategia: Descuento VIP
class VIPDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.80  # 20% de descuento

# Estrategia: Sin descuento
class NoDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount  # No se aplica descuento
