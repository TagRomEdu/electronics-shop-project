from src.keyboard import Keyboard


kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang():
    kb.change_lang()
    assert kb.language == 'RU'
