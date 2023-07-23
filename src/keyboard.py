from src.item import Item


class MixinChange:
    """Миксин класс для реализации смены языка клавиатуры"""

    def change_lang(self):
        if self.language == 'RU':
            self.language == 'EN'
            return self.language


class Keyboard(Item, MixinChange):
    def __init__(self, name, price, quantity, language):
        super().__init__(name, price, quantity)
        self.language = language


kb = Keyboard('Dark Project KD87A', 9600, 5)
str(kb) == "Dark Project KD87A"
