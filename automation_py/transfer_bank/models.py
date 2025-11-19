from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Account:
    email: str
    balance: Decimal

    def debitar(self, amount: Decimal):
        if amount <= 0:
            raise ValueError("El monto debe ser mayor a 0")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente")
        self.balance -= amount
    
    def acreditar(self, amount: Decimal):
        if amount <= 0:
            raise ValueError("El monto debe ser mayor a 0")
        self.balance += amount

@dataclass
class Transfer:
    origin: Account
    destination: str
    amount: Decimal
    state: str = "pending"
    
    def apply(self):
        self.origin.debitar(self.amount)
        self.state = "aplicated"
        