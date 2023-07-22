from src.item import Item


ex1 = Item("name", 10, 5)
ex2 = Item("Смартфон", 10000, 20)

def test_Item():
    assert ex1.name == "name"
    assert ex1.price == 10
    assert ex1.quantity == 5
    assert len(Item.all) == 2


def test_calculate_total_price():
    assert ex1.calculate_total_price() == 50


def test_apply_discount():
    ex1.pay_rate = 2
    ex1.apply_discount()
    assert ex1.price == 20


def test_instantiate_from_csv():
    assert print(Item.instantiate_from_csv()) is None


def test_string_to_number():
    assert Item.string_to_number('8.1234') == 8


def test_repr():
    assert repr(ex2) == "Item('Смартфон', 10000, 20)"


def test_str():
    assert str(ex2) == 'Смартфон'

def test_add():
    assert ex1 + ex2 == 25
