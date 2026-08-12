"""Упражнение В — тест(ы) на фикстуру-фабрику. См. TASK.md, часть В.

Сложности (ученик):
- Долго не было прямой фразы: внутри фикстуры нужен ещё один def, return его без ().
- Путали параметры фикстуры (для pytest это другие фикстуры) и аргументы внутренней функции.
- return make_post vs return make_post() — «машина» vs «уже готовая чашка».
- title/body сначала повесили на фикстуру → TypeError unexpected keyword argument 'title'.
"""


def test_fabric(make_post):
    spisok = []
    p1 = make_post(title="Создаём первого клиента")
    spisok.append(p1)
    p2 = make_post(title="Создаём второго клиента")
    spisok.append(p2)
    assert len(spisok) == 2


# --- вариант почище (коуч), твой код выше не трогаем ---
# def test_fabric(make_post):
#     p1 = make_post(title="Создаём первого клиента")
#     p2 = make_post(title="Создаём второго клиента")
#     # make_post() без аргументов тоже должен работать (дефолты во внутренней функции)
#     p3 = make_post()
#     assert isinstance(p1, dict) and "id" in p1
#     assert isinstance(p2, dict) and "id" in p2
#     assert isinstance(p3, dict) and "id" in p3
#     assert len([p1, p2, p3]) == 3
