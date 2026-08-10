"""safe_divide — блок 1.2."""

def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Делитель == 0")
    else:
        return a / b