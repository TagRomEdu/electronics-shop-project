from src.item import Item


class MixinChange:

    """Миксин класс для реализации смены языка клавиатуры"""

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):

        """Возвращает экземпляр класса с изменной раскладкой языка.
        Так нужно, чтобы можно было применять метод несколько раз: kb.change_lang().change_lang()"""

        self.__language = 'RU' if self.__language == 'EN' else 'EN'
        return self


class Keyboard(Item, MixinChange):

    """Класс для кдавиатур"""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinChange.__init__(self)
