from banking_class import DepositCalculator

def main():
    """Основная функция для взаимодействия с пользователем"""
    amount = float(input("Введите сумму вклада: "))
    duration = int(input("Введите срок (лет): "))

    calculator = DepositCalculator(amount, duration)
    results = calculator.calculate_all()

    print("\nПрогнозируемая прибыль:")
    for name, profit in results.items():
        print(f"{name}: {profit:.2f} ₽")


if __name__ == "__main__":
    main()