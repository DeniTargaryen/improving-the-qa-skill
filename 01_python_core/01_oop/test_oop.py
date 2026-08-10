import pytest

from account import Account
from jsonplaceholder_api import JsonPlaceholderApi
from money import Money
from rectangle import Rectangle


class TestAccount:
    def test_init_default_balance(self):
        acc = Account("Ann")
        assert acc.owner == "Ann"
        assert acc.balance == 0

    def test_deposit_and_withdraw(self):
        acc = Account("Bob", 100)
        acc.deposit(50)
        assert acc.balance == 150
        acc.withdraw(20)
        assert acc.balance == 130

    def test_withdraw_too_much_raises(self):
        acc = Account("Bob", 100)
        with pytest.raises(ValueError):
            acc.withdraw(999)

    def test_deposit_non_positive_raises(self):
        acc = Account("Bob", 10)
        with pytest.raises(ValueError):
            acc.deposit(0)


class TestRectangle:
    def test_area(self):
        assert Rectangle(3, 4).area() == 12

    def test_from_square(self):
        r = Rectangle.from_square(5)
        assert isinstance(r, Rectangle)
        assert r.width == 5
        assert r.height == 5

    def test_is_valid(self):
        assert Rectangle.is_valid(2, 3) is True
        assert Rectangle.is_valid(0, 3) is False
        assert Rectangle.is_valid(-1, 2) is False


class TestMoney:
    def test_eq_same(self):
        assert Money(100, "RUB") == Money(100, "RUB")

    def test_eq_different(self):
        assert Money(100, "RUB") != Money(200, "RUB")
        assert Money(100, "RUB") != Money(100, "USD")

    def test_eq_not_money(self):
        assert (Money(1, "RUB") == 1) is False

    def test_repr(self):
        text = repr(Money(100, "RUB"))
        assert "100" in text
        assert "RUB" in text


class TestJsonPlaceholderApi:
    def test_inherits_and_sets_base_url(self):
        api = JsonPlaceholderApi()
        assert isinstance(api, JsonPlaceholderApi)
        assert api.base_url == "https://jsonplaceholder.typicode.com"
