from strategy import DiscountStrategy

# Contexto que usa estrategias
class DiscountContext:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate_discount(self, amount: float) -> float:
        return self.strategy.calculate(amount)
