from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class BankAccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Fondos insuficientes")
        self.balance -= amount
        print(f"Retirados {amount}. Nuevo saldo: {self.balance}")

class CreditAccount(Account):
    def __init__(self, balance, credit_limit):
        self.balance = balance
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if amount > (self.balance + self.credit_limit):
            raise ValueError("Excede el límite de crédito")
        self.balance -= amount
        print(f"Retirados {amount}. Nuevo saldo: {self.balance} (incluido crédito)")
