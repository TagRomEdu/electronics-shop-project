from csv import DictReader
import os


CSV_PATH = os.path.join('/', '0_programming_python', 'electronics-shop-project', 'src', 'items.csv')


class Item:
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
    def instantiate_from_csv(cls) -> list:
        """
        Собирает инфу из CSV файла и создаёт на её основе экземпляр класса
        """
        cls.all = []
        dict_lst = []
        with open(CSV_PATH) as file:
            reader = DictReader(file)
            for reads in reader:
                dict_lst.append(reads)
        for dictnry in dict_lst:
            cls(dictnry['name'], dictnry['price'], dictnry['quantity'])
        return cls.all

    @staticmethod
    def string_to_number(num: str) -> int:
        """
        Переводит строку в число
        """
        return int(float(num))
