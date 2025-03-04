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


class PepperoniPizza(Pizza):
    """
    Класс, представляющий пиццу Пепперони.
    """

    def __init__(self):
        """
        Инициализирует пиццу Пепперони с заданными атрибутами.
        """
        super().__init__("Пепперони", "Тонкое", "Томатный", ["Пепперони", "Сыр"], 10.99)


class BBQPizza(Pizza):
    """
    Класс, представляющий BBQ-пиццу.
    """

    def __init__(self):
        """
        Инициализирует BBQ-пиццу с заданными атрибутами.
        """
        super().__init__("BBQ Пицца", "Толстое", "Барбекю", ["Курица", "Лук", "Сыр"], 12.99)


class SeafoodPizza(Pizza):
    """
    Класс, представляющий морепродуктовую пиццу.
    """

    def __init__(self):
        """
        Инициализирует пиццу с морепродуктами с заданными атрибутами.
        """
        super().__init__("Морепродукты", "Обычное", "Белый соус", ["Креветки", "Мидии", "Сыр"], 14.99)


class Order:
    """
    Класс, представляющий заказ клиента, содержащий несколько пицц.
    """
    order_counter = 0

    def __init__(self):
        """
        Инициализирует пустой заказ и присваивает уникальный номер.
        """
        self.ordered_pizzas = []
        Order.order_counter += 1
        self.order_number = Order.order_counter

    def __str__(self):
        """
        Возвращает строковое представление заказа.
        """
        return f"\nЗаказ {self.order_number}: {len(self.ordered_pizzas)} пицц, Итого: ${self.total()}"

    def add_pizza(self, pizza):
        """
        Добавляет пиццу в заказ.
        """
        self.ordered_pizzas.append(pizza)

    def total(self):
        """
        Рассчитывает и возвращает общую стоимость заказа.
        """
        return sum(pizza.price for pizza in self.ordered_pizzas)

    def process(self):
        """
        Обрабатывает заказ: готовит, выпекает, нарезает и упаковывает все пиццы.
        """
        print(f"Обрабатываем {self}...")
        for pizza in self.ordered_pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()


class Terminal:
    """
    Класс, представляющий терминал для взаимодействия с клиентами.
    """

    def __init__(self):
        """
        Инициализирует терминал с предустановленным меню и пустым заказом.
        """
        self.menu = [PepperoniPizza(), BBQPizza(), SeafoodPizza()]
        self.order = None

    def show_menu(self):
        """
        Отображает доступные пиццы в меню.
        """
        print("Меню:")
        for i, pizza in enumerate(self.menu, start=1):
            print(f"{i}. {pizza}")

    def handle_command(self, choice):
        """
        Обрабатывает выбор клиента и добавляет соответствующую пиццу в заказ.
        """
        if choice in range(1, len(self.menu) + 1):
            self.order.add_pizza(self.menu[choice - 1])
            print(f"Добавлено: {self.menu[choice - 1].name}")

    def accept_payment(self):
        """
        Симулирует обработку платежа.
        """
        print(f"Получено ${self.order.total()}. Спасибо!")

    def run(self):
        """
        Запускает терминал, позволяя клиентам делать заказы в интерактивном режиме.
        """
        self.order = Order()
        self.show_menu()
        while True:
            choice = input("\nВведите номер пиццы для добавления в заказ (или 'done' для завершения): ")
            if choice.lower() == "done":
                break
            if choice.isdigit() and 1 <= int(choice) <= len(self.menu):
                self.handle_command(int(choice))
            else:
                print("Неверный выбор. Попробуйте снова.")
        print(self.order)
        self.accept_payment()
        self.order.process()


if __name__ == "__main__":

    terminal = Terminal()
    terminal.run()