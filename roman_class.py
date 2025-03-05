"""
Класс Roman представляет работу с римскими числами, поддерживая базовые арифметические операции.
"""

class Roman:
    """Класс для работы с римскими числами."""

    def __init__(self, value):
        """
        Инициализирует объект римского числа.

        Параметры:
            value (str | int): Строка с римским числом или целое число от 1 до 3999.

        Исключения:
            ValueError: При некорректных символах, значении или типе.
            TypeError: Если передан не строковый или целочисленный тип.
        """
        if isinstance(value, str):
            self.__value = self.__from_roman(value)
        elif isinstance(value, int):
            if 1 <= value <= 3999:
                self.__value = value
            else:
                raise ValueError(f"Число {value} вне допустимого диапазона (1-3999)")
        else:
            raise TypeError("Аргумент должен быть строкой или целым числом")

    @staticmethod
    def __int_to_roman(value):
        """Приватный статический метод для конвертации целого числа в римскую запись."""
        if not (1 <= value <= 3999):
            raise ValueError(f"Число {value} вне диапазона 1-3999")

        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (
            m[value // 1000] +
            c[(value % 1000) // 100] +
            x[(value % 100) // 10] +
            i[value % 10]
        )

    def __from_roman(self, roman_str):
        """Приватный метод для конвертации римской записи в целое число."""
        total = 0
        prev_value = 0

        for char in reversed(roman_str.upper()):
            current_value = self.__from_single_roman(char)
            total += current_value if current_value >= prev_value else -current_value
            prev_value = current_value

        if self.__int_to_roman(total) != roman_str.upper():
            raise ValueError(f"Некорректная римская запись: {roman_str}")

        return total

    @staticmethod
    def __from_single_roman(char):
        """Возвращает значение одиночного римского символа."""
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        if char in roman_values:
            return roman_values[char]
        raise ValueError(f"Недопустимый символ: {char}")

    def __add__(self, other):
        """Возвращает новый объект Roman с суммой значений."""
        return Roman(self.__value + other.__value)

    def __sub__(self, other):
        """Возвращает новый объект Roman с разностью значений."""
        return Roman(self.__value - other.__value)

    def __truediv__(self, other):
        """Возвращает новый объект Roman с целочисленным частным."""
        return Roman(self.__value // other.__value)

    def __mul__(self, other):
        """Возвращает новый объект Roman с произведением значений."""
        return Roman(self.__value * other.__value)

    def __str__(self):
        """Возвращает строковое представление в виде римского числа."""
        return self.__int_to_roman(self.__value)

# Примеры использования
a = Roman("XX")    # 20
b = Roman("VII")   # 7
print(a + a)       # XL (40)
print(a - b)       # XIII (13)
print(a / b)       # II (2)
print(a * b)       # CXL (140)
