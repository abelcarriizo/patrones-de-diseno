from abc import ABC, abstractmethod

class Observer(ABC):  # Interfaz
    @abstractmethod
    def update(self, message: str):
        pass
    