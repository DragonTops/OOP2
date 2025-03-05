class Deposit:
    """Базовый класс для банковских вкладов

    Attributes:
        amount (float): Сумма вклада
        duration (int): Срок вклада в годах
        rate (float): Годовая процентная ставка
    """

    def __init__(self, amount, duration, rate):
        self.amount = amount
        self.duration = duration
        self.rate = rate

    def calculate_profit(self):
        """Рассчитывает прибыль по вкладу

        Raises:
            NotImplementedError: Если метод не переопределен в подклассе
        """
        raise NotImplementedError("Метод должен быть переопределен в подклассе")


class FixedDeposit(Deposit):
    """Срочный вклад с простыми процентами

    Формула расчета: P = amount * rate * duration / 100
    """

    def calculate_profit(self):
        """Возвращает прибыль по формуле простых процентов"""
        return self.amount * self.rate * self.duration / 100


class BonusDeposit(Deposit):
    """Бонусный вклад с дополнительной премией от прибыли

    Attributes:
        bonus_rate (float): Процент бонуса от основной прибыли
        threshold (float): Минимальная сумма для получения бонуса
    """

    def __init__(self, amount, duration, rate, bonus_rate, threshold):
        super().__init__(amount, duration, rate)
        self.bonus_rate = bonus_rate
        self.threshold = threshold

    def calculate_profit(self):
        """
        Рассчитывает прибыль с учетом бонуса:
        1. Основная прибыль по простым процентам
        2. Бонус: bonus_rate% от прибыли, если сумма > threshold
        """
        base_profit = self.amount * self.rate * self.duration / 100
        bonus = base_profit * self.bonus_rate / 100 if self.amount > self.threshold else 0
        return base_profit + bonus


class CapitalizationDeposit(Deposit):
    """Вклад с ежемесячной капитализацией процентов

    Формула расчета: 
        total = amount * (1 + monthly_rate) ** months
        profit = total - amount
    где:
        monthly_rate = годовая ставка / 12 / 100
        months = срок в годах * 12
    """

    def calculate_profit(self):
        """Рассчитывает прибыль с учетом ежемесячной капитализации"""
        months = self.duration * 12
        monthly_rate = self.rate / 100 / 12
        total = self.amount * (1 + monthly_rate) ** months
        return total - self.amount