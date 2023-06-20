from src.item import Item
from src.mixin_lang import MixinLang


class KeyBoard(Item, MixinLang):
    '''
    Класс, который создаёт объекты
    клавиатура
    '''

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)