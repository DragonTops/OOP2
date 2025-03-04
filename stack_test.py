from stack_class import Stack

if __name__ == "__main__":
    print("Создание стека и добавление элементов:")
    s = Stack()
    s.push(1)
    s.push(2)
    print(s)  # Stack([2, 1])

    print("\nИзвлечение элемента:")
    print(s.pop())  # 2
    print("Верхний элемент после pop:", s.peek())  # 1

    print("\nСоздание стека из строки:")
    s2 = Stack.from_string("3, 4, five")
    print(s2)  # Stack(['five', 4, 3])

    print("\nСложение двух стеков:")
    s3 = s + s2
    print(s3)  # Stack(['five', 4, 3, 1])

    print("\nСохранение стека в файл и загрузка:")
    s3.save("stack.json")
    s4 = Stack()
    s4.load("stack.json")
    print("Загруженный стек:", s4)  # Stack(['five', 4, 3, 1])

    print("\nПроверка размера и пустоты:")
    print("Размер s4:", s4.size())  # 4
    print("Пуст ли s4?", s4.is_empty())  # False
    s4.clear()
    print("Пуст ли s4 после очистки?", s4.is_empty())  # True

    print("\nПроверка наличия элемента:")
    print("3 в s2?", 3 in s2)  # True
    print("'five' в s2?", 'five' in s2)  # True
    print("5 в s2?", 5 in s2)  # False