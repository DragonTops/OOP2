import json


class Stack:
    """Класс, реализующий структуру данных стек (LIFO - Last In, First Out).

    Атрибуты:
        items (list): Список элементов стека. Последний элемент списка считается вершиной стека.

    Методы:
        push(item): Добавляет элемент на вершину стека.
        pop(): Удаляет и возвращает верхний элемент стека.
        peek(): Возвращает верхний элемент без удаления.
        is_empty(): Проверяет, пуст ли стек.
        size(): Возвращает количество элементов в стеке.
        clear(): Очищает стек.
        from_string(cls, str_value): Создает стек из строки.
        save(filename): Сохраняет стек в JSON-файл.
        load(filename): Загружает стек из JSON-файла.
    """

    def __init__(self, items=None):
        """Инициализирует стек.

        Args:
            items (list, optional): Начальные элементы стека. По умолчанию None.
        """
        self.items = items.copy() if items else []

    def __str__(self):
        """Возвращает строковое представление стека в формате: Stack([элементы_сверху_вниз])."""
        return f"Stack({self.items[::-1]})"

    def push(self, item):
        """Добавляет элемент на вершину стека.

        Args:
            item: Элемент для добавления (любого типа).
        """
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает верхний элемент стека.

        Returns:
            Элемент с вершины стека.

        Raises:
            IndexError: Если стек пуст.
        """
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        """Возвращает верхний элемент стека без его удаления.

        Returns:
            Элемент с вершины стека или None, если стек пуст.
        """
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        """Проверяет, пуст ли стек.

        Returns:
            bool: True, если стек пуст, иначе False.
        """
        return len(self.items) == 0

    def size(self):
        """Возвращает количество элементов в стеке.

        Returns:
            int: Размер стека.
        """
        return len(self.items)

    def __add__(self, other):
        """Объединяет два стека, создавая новый стек.

        Элементы второго стека добавляются поверх элементов первого.

        Args:
            other (Stack): Второй стек для объединения.

        Returns:
            Stack: Новый стек, содержащий все элементы.
        """
        return Stack(self.items + other.items)

    @classmethod
    def from_string(cls, str_value):
        """Создает стек из строки с элементами, разделенными запятыми.

        Элементы преобразуются в целые числа, если возможно, иначе остаются строками.

        Args:
            str_value (str): Строка с элементами (например, "3, 4, five").

        Returns:
            Stack: Стек с элементами из строки.
        """
        items = []
        for item in str_value.split(','):
            stripped = item.strip()
            try:
                items.append(int(stripped))
            except ValueError:
                items.append(stripped)
        return cls(items)

    def save(self, filename):
        """Сохраняет элементы стека в JSON-файл.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w') as f:
            json.dump(self.items, f)

    def load(self, filename):
        """Загружает элементы стека из JSON-файла.

        Args:
            filename (str): Имя файла для загрузки.
        """
        with open(filename, 'r') as f:
            self.items = json.load(f)

    def clear(self):
        """Очищает стек, удаляя все элементы."""
        self.items.clear()

    def __contains__(self, item):
        """Проверяет, содержится ли элемент в стеке.

        Args:
            item: Элемент для поиска.

        Returns:
            bool: True, если элемент найден, иначе False.
        """
        return item in self.items