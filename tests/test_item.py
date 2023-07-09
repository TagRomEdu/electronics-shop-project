from src.item import Item


ex1 = Item("name", 10, 5)


def test_Item():
    assert ex1.name == "name"
    assert ex1.price == 10
    assert ex1.quantity == 5
    assert len(Item.all) == 1


def test_calculate_total_price():
    assert ex1.calculate_total_price() == 50


def test_apply_discount():
    ex1.pay_rate = 2
    ex1.apply_discount()
    assert ex1.price == 20