"""
Модуль для расчета прибыли по различным банковским вкладам.
Реализует следующие типы вкладов:
- Срочный вклад с простыми процентами
- Бонусный вклад с дополнительной премией
- Вклад с ежемесячной капитализацией процентов
"""
from deposit_types import FixedDeposit, BonusDeposit, CapitalizationDeposit


class DepositCalculator:
    """Класс для сравнения различных типов вкладов

    Attributes:
        deposits (dict): Словарь с предустановленными параметрами вкладов
    """

    def __init__(self, amount, duration):
        """
        Args:
            amount (float): Сумма вклада
            duration (int): Срок вклада в годах
        """
        self.amount = amount
        self.duration = duration
        self.deposits = {
            "Срочный вклад": FixedDeposit(amount, duration, 5),
            "Бонусный вклад": BonusDeposit(amount, duration, 4, 10, 100000),
            "Капитализация": CapitalizationDeposit(amount, duration, 4.5)
        }

    def calculate_all(self):
        """Возвращает прибыль для всех типов вкладов

        Returns:
            dict: Словарь {название вклада: прибыль}
        """
        return {name: dep.calculate_profit() for name, dep in self.deposits.items()}
