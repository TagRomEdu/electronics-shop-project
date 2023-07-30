from csv import DictReader
from src.ifc import InstantiateCSVError
import os


class Item:
    CSV_PATH = os.path.join(os.path.dirname(__file__), 'items.csv')
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Собирает инфу из CSV файла и создаёт на её основе экземпляр класса
        """
        try:
            cls.all = []
            with open(cls.CSV_PATH) as file:
                reader = DictReader(file)
                for reads in reader:
                    cls(reads['name'], reads['price'], reads['quantity'])
        except FileNotFoundError:
            print("Отсутствует файл items.csv")
        except KeyError:
            raise InstantiateCSVError from None

    @staticmethod
    def string_to_number(num: str) -> int:
        """
        Переводит строку в число
        """
        return int(float(num))

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError("It's only for Item objects!")
