from src.item import Item


class MixinChange:
    """Миксин класс для реализации смены языка клавиатуры"""
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        self.__language = 'RU' if self.__language == 'EN' else 'EN'
        return self


class Keyboard(Item, MixinChange):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinChange.__init__(self)
