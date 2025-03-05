class Pizza:
    """
    Базовый класс, представляющий пиццу с её атрибутами и методами.
    """

    def __init__(self, name, dough, sauce, toppings, price):
        """
        Инициализирует пиццу с названием, типом теста, соусом, начинками и ценой.
        """
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price

    def __str__(self):
        """
        Возвращает строковое представление пиццы.
        """
        return f"{self.name} на {self.dough} тесте, соус {self.sauce}, начинки: {', '.join(self.toppings)}. Цена: ${self.price}"

    def prepare(self):
        """
        Симулирует процесс подготовки пиццы.
        """
        print(f"Подготавливаем {self.name}...\n")

    def bake(self):
        """
        Симулирует процесс выпекания пиццы.
        """
        print(f"Выпекаем {self.name}...\n")

    def cut(self):
        """
        Симулирует нарезку пиццы.
        """
        print(f"Режем {self.name}...\n")

    def pack(self):
        """
        Симулирует упаковку пиццы.
        """
        print(f"Упаковываем {self.name}...\n")
