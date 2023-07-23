from src.item import Item


class Keybord(Item):
    def __init__(self, name, price, quantity, lang):
        super().__init__(name, price, quantity)
        self.lang = lang
