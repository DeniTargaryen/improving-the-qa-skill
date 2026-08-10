# Rectangle — что делать (минимум)

Ты уже понял Account: объект хранит поля, методы их меняют/читают.

`Rectangle` — тоже объект, только поля другие: **ширина** и **высота**.

## Обычные методы (как deposit)

- `__init__(self, width, height)` — сохранить `self.width`, `self.height`
- `area(self)` — **вернуть** число `width * height` (не None)

## Два новых слова

### `@staticmethod` — `is_valid(width, height)`

Функция «лежит в классе», но **объект не нужен**.  
Вызов: `Rectangle.is_valid(2, 3)` — без `Rectangle(2, 3)`.

Что возвращает: `True`, если оба числа **> 0**, иначе `False`.

Зачем: проверка «можно ли такой прямоугольник», ещё до создания.

### `@classmethod` — `from_square(cls, side)`

Фабрика: «сделай Rectangle из квадрата».  
`cls` — это сам класс (`Rectangle`), не экземпляр.

Что возвращает: **новый** объект, примерно как `cls(side, side)`  
(квадрат = ширина и высота одинаковые).

Вызов: `Rectangle.from_square(5)` → прямоугольник 5×5.

## Порядок работы

1. Допиши `__init__` + `area`  
2. Потом `is_valid`  
3. Потом `from_square`  

```bash
python -m pytest 01_python_core/01_oop/test_oop.py::TestRectangle -v
```
