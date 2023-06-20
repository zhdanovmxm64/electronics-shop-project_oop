import os.path
import pytest

from src.item import Item
from src.phone import Phone
from src.exceptions import InstantiateCSVError


@pytest.fixture
def make_item():
    return Item("Телевизор", 3000, 4)


def test_init(make_item):
    item = make_item
    assert item.name == "Телевизор"
    assert item.price == 3000
    assert item.quantity == 4


def test_calculate_total_price(make_item):
    item = make_item
    assert item.calculate_total_price() == 12_000
    assert item.calculate_total_price() == item.price * item.quantity


def test_apply_discount(make_item):
    item = make_item
    first_price = item.price
    item.apply_discount()
    assert item.price == first_price * Item.pay_rate
    assert item.price == 3000.0

    item.price = first_price
    item.pay_rate = 1.2
    item.apply_discount()
    assert item.price == first_price * item.pay_rate
    assert item.price == 3600.0


def test_all(make_item):
    for i in Item.all:
        assert isinstance(i, object)


def test_set_name(make_item, capsys):
    item = make_item
    item.name = "Name"
    assert item.name == "Name"

    item.name = "NameNameNameNameName"
    output = capsys.readouterr()
    assert output.out == "Длина названия товара не " \
                         "должна превышать 10 символов\n"
    item.name = ""
    output = capsys.readouterr()
    assert output.out == "Длина названия должна иметь " \
                         "хотябы 1 символ\n"


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)
    assert str(Item.all[4]) == "Клавиатура"

    Item.CSV = "NOT_FOUND"
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()

    Item.CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()



def test_string_to_number():
    string = "343"
    assert Item.string_to_number(string) == 343


def test_repr(make_item):
    item = make_item
    assert repr(item) == "Item('Телевизор', 3000, 4)"


def test_str(make_item):
    item = make_item
    assert str(item) == "Телевизор"


def test_add(make_item):
    item = make_item
    phone = Phone('Iphone', 15_000, 3, 1)

    assert item + item == 8
    assert item + phone == 7