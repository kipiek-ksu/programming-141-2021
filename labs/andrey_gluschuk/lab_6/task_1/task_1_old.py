"""
     Глущук Андрій 141
     Лабораторна робота №6
     Завдання 1
 5. Описати функцію RectPS (x1, y1, x2, y2, P, S), яка обчислює периметр P і площу
S прямокутника зі сторонами, паралельними осям координат, за координатами
(x1, y1), (x2, y2) його протилежних вершин (x1, y1, x2, y2 - вхідні, P і S - вихідні
параметри дійсного типу). За допомогою цієї функції знайти периметри і площі
трьох прямокутників з даними протилежними вершинами.
"""


def rectPS(x1, y1, x2, y2):
    P = ((x2 - x1) + (y2 - y1)) * 2
    S = (x2 - x1) * (y2 - y1)
    return P, S


for i in range(3):
    x1 = float(input("X1: "))
    x2 = float(input("X2: "))
    y1 = float(input("Y1: "))
    y2 = float(input("Y2: "))
    P, S = rectPS(x1, y1, x2, y2)
    if P > 0 and S > 0:
        print("P = ", P, "\nS = ", S)
    else:
        print("shoto ne to")