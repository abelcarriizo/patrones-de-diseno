from abc import ABC, abstractmethod

# Interfaz Estrategia
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass
