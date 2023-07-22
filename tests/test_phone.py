from src.phone import Phone


ex1 = Phone("name", 10, 5, 2)
ex2 = Phone("Смартфон", 10000, 20, 1)


def test_phone():
    assert ex1.name == "name"
    assert ex1.price == 10
    assert ex1.quantity == 5
    assert ex1.number_of_sim == 2


def test_repr():
    assert repr(ex2) == "Phone('Смартфон', 10000, 20, 1)"


def test_number_of_sim():
    ex2.number_of_sim = 2
    assert ex2.number_of_sim == 2