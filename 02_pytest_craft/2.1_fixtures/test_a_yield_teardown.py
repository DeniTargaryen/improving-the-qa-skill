"""Упражнение А — тест(ы) на фикстуру с yield и teardown. См. TASK.md, часть А."""


def test_a(setup):
    resp = setup
    # Порядок: сначала тип объекта, потом ключи (если resp не dict — падение понятнее).
    assert isinstance(resp, dict)
    assert "id" in resp
    assert isinstance(resp["id"], int)
    # == 101 завязано на jsonplaceholder; для сдачи А достаточно наличия id.
    # На работе так не хардкодь id чужого API без нужды.
    assert resp["id"] == 101
