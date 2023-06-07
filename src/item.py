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
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price: float = self.price * self.quantity
        return total_price

    @property
    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return None

    @property
    def name(self) -> str:
        """
        Возвращает название товара
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Присваивает атрибуту name значение new_name,
        при условии, что длина названия товара не больше 10 символов
        """
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception(f'Длина наименования товара "{new_name}" превышает 10 символов')
    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        with open('../src/items.csv') as csvfile:
            item = csv.DictReader(csvfile)
            for row in item:
                cls(row['name'], row['price'], row['quantity'])
    @staticmethod
    def string_to_number(file):
        return int(float(file))