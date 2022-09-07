import math


while True:
    print("Нахождение S и P")
    print("1. Треугольника")
    print("2. Круга")
    print("3. Прямоугольника")
    print("0. Выйти из программы")
    cmd = input("Выберите пункт: ")

    if cmd == "1":
        while True:
            print("Выбор треугольника")
            print("1. Через гипотенузу и острый угол (Прямой)")
            print("2. Через основание и высоту (Равнобедренный)")
            print("3. По средней линии (Равносторонний)")
            print("4. По координатом трёх вершин")
            print("0. Назад")
            cm = input("Выберите пункт: ")

            if cm == "1":
                c = float(input("Гипотенуза = "))
                alf = int(input("Острый угол = "))
                if (c > 0 and 0 < alf < 90):
                    s = (1 / 4 * c * c * math.sin(math.radians(2*alf)))
                    b = c * math.cos(math.radians(alf))
                    a = c * math.sin(math.radians(alf))
                    print("P =", a + b + c)
                    print("S =", s)
                else:
                    print("Вы ввели неверное значение!")

            elif cm == "2":
                a = float(input("Основание = "))
                h = float(input("Высота = "))
                if (h > 0 and a > 0):
                    s = (1 / 2 * (a * h))
                    ac = math.sqrt((a/2)**2 + h*h)
                    print("P =", ac + a + ac)
                    print("S =", s)
                else:
                    print("Вы ввели неверное значение!")

            elif cm == "3":
                mn = float(input("Средняя линия = "))
                if (mn > 0):
                    s = (mn*mn * math.sqrt(3))
                    p = mn * 6
                    print("P =", p)
                    print("S =", s)
                else:
                    print("Вы ввели неверное значение!")

            elif cm == "4":
                print("Первая вершина")
                x1, y1 = map(float, input().split())
                print("Вторая вершина")
                x2, y2 = map(float, input().split())
                print("Третья вершина")
                x3, y3 = map(float, input().split())
                a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
                c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
                p = (a + b + c) / 2.0
                s = math.sqrt(p * (p - a) * (p - b) * (p - c))
                print("S =", s, "\nP =", a + b + c)

            elif cm == "0":
                break
            else:
                print("Вы ввели неверное значение")

    elif cmd == "2":
        r = float(input("Радиус = "))
        if (r > 0):
            print("Длина окружности =", 2 * math.pi * r)
            print("S =", math.pi * r * r)
        else:
            print("Радиус окружности должен быть положительным числом!")

    elif cmd == "3":
        a = float(input("Длина = "))
        b = float(input("Ширина = "))
        if (a > 0 and b > 0):
            print("S =", a * b)
            print("P =", a + b)
        else:
            print("Длина и ширина прямоугольника должны быть положительными числами!")

    elif cmd == "0":
        break
    else:
        print("Вы ввели неверное значение")