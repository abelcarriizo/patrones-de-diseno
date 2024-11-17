class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """Resta dinero del saldo."""
        if amount > self.balance:
            raise ValueError("Fondos insuficientes")
        self.balance -= amount
        print(f"Retirados {amount}. Nuevo saldo: {self.balance}")

class CreditAccount(BankAccount):
    def __init__(self, balance, credit_limit):
        super().__init__(balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        """Permite retirar hasta el límite de crédito."""
        if amount > (self.balance + self.credit_limit):
            raise ValueError("Excede el límite de crédito")
        self.balance -= amount
        print(f"Retirados {amount}. Nuevo saldo: {self.balance} (incluido crédito)")
