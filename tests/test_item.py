import pytest
import pytest as pytest

from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""
@pytest.fixture
def item_fixture():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price(item_fixture):
    assert item_fixture.calculate_total_price() == 200000

def test_string_to_number():
    assert Item.string_to_number('15') == 15
    assert Item.string_to_number('25.0') == 25
    assert Item.string_to_number('35.5') == 35

def test_apply_discount(item_fixture):
    Item.pay_rate = 0.8
    item_fixture.apply_discount
    assert item_fixture.price == 8000.0

def test___repr__(item_fixture):
    assert repr(item_fixture) == "Item('Смартфон', 10000, 20)"

def test___str__(item_fixture):
    assert str(item_fixture) == 'Смартфон'
