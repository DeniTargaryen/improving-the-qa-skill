"""Блок 3.2. Свои классы ошибок — по TASK.md.

Это те же имена, что в 1.2 (`ApiError`/`NotFoundError`), но теперь их реально
использует negative_api.py в этой же папке — не «ярлык в вакууме», а рабочий
код клиента.

Файл называется api_errors.py, а не exceptions.py — в репозитории уже есть
одноимённый модуль (01_python_core/01_exceptions/exceptions.py), и без
пакетов с __init__.py общий прогон pytest по всему репо закэшировал бы
только первый импортированный exceptions и подставил его везде (тихий баг).
"""

# ApiError(Exception) и NotFoundError(ApiError) — напиши сам, как в 1.2.

class ApiError(Exception):
    pass

class NotFoundError(ApiError):
    pass