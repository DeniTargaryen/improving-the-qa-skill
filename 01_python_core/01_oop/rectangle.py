"""Блок 1.1 — реализуй класс Rectangle."""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        wh = self.width * self.height
        return wh

    @classmethod
    def from_square(cls, side):
        #Rectangle(side, side)
        return Rectangle(side, side)

    @staticmethod
    def is_valid(width, height) -> bool:
        if width <= 0 or height <= 0:
            return False
        return True
