from src.item import Item


class MixinChange:
    """Миксин класс для реализации смены языка клавиатуры"""
    lang = 'EN'

    def __init__(self):
        self.language = self.lang

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
            return self.language
        self.language = 'EN'
        return self.language


class Keyboard(Item, MixinChange):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'


kb = Keyboard('Dark Project KD87A', 9600, 5)
print(str(kb))
print(kb.__dict__)
print(kb.change_lang())
print(kb.__dict__)
print(kb.change_lang())