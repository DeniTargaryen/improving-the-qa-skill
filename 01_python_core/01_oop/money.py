"""Блок 1.1 — реализуй класс Money."""


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other) -> bool:
        if isinstance(other, Money):
            if self.amount == other.amount and self.currency == other.currency:
                return True
        return False

    def __repr__(self) -> str:
        return f'Money(Сумма:{self.amount}, Валюта:{self.currency})'
