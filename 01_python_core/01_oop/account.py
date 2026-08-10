"""Блок 1.1 — класс Account."""


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount) -> None:
        if amount <= 0 or amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
