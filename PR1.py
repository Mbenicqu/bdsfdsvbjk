while (1):
    Res = 0
    print("Выберете математическое действие:\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление\n")
    qwerty = input()
    print("Введите количество цифр, которое вы собираетесь вводить")
    amount = int(input())
    if (qwerty == "1"):
        print("Введите числа:")
        for i in range(amount):
            a = float(input())
            Res += a
            i += i
        print(f"Ответ: {Res}")
    elif (qwerty == "2"):
        print("Введите числа:")
        for i in range(amount):
            a = float(input())
            if (i == 0):
                Res = a
            else:
                Res -= a
            i += i
        print(f"Ответ: {Res}")
    elif (qwerty == "3"):
        print("Введите числа:")
        for i in range(amount):
            a = float(input())
            if (i == 0):
                Res = a
            else:
                Res *= a
            i += i
        print(f"Ответ: {Res}")
    elif (qwerty == "4"):
        print("Введите числа:")
        for i in range(amount):
            a = float(input())
            if (i == 0):
                Res = a
            else:
                if (i != 0):
                    if (a == 0):
                        print("Стоямба, делить на нуль нельзя. Здесь мы и остановимся")
                        break
                else:
                    Res /= a
            i += i
        print(f"Ответ: {Res}")
    else:
        print("Такого варианта нет, давай-ка по-новой\n")