"""
7. За довжинами двох сторін деякого трикутника і кутом між ними знайти довжину третьої сторони і площу цього трикутника.
11. Знайти значення функції y=3x6+6x2+7 при даному значенні x.
15. Дано змінні A, B, C. Змінити їх значення, перемістивши вміст A в B, B - в C, C - в A, і вивести нові значення змінних A, B, C.
19. Знайти корені квадратного рівняння A · x2 + B · x + C = 0, заданого своїми коефіцієнтами A, B, C (A>0), якщо відомо, що дискримінант рівняння позитивний. Вивести спочатку менший, а потім більший із знайдених коренів. Коріння квадратного рівняння знаходяться за формулою x1, 2 =
(−B ± (D)1/2)/(2·A), де D - дискримінант, що дорівнює B2 − 4·A·C.
3. Дано два ненульових числа. Знайти суму, різницю, добуток і частку їх квадратів.
"""

ST = "p"
while(ST != "stop"):
    print("Выбери числом какую задачу запустить...\n Выбор: 3, 7, 11, 15, 19\n")
    Number = int(input())
    if(Number == 3):
        #Дано два ненульових числа. Знайти суму, різницю, добуток і частку їх квадратів.
        A = int(input("Введите первое число: "))
        if (A == 0):
            print("Ноль не подходит... Введите целое число: ")
            A = int(input())
        B = int(input("Введите второе число: "))
        if (B == 0):
            print("Ноль не подходит... Введите целое число: ")
            B = int(input())
        Sum = A + B
        Riz = A - B
        Dob = A * B
        CHkv = pow(A, 2) / pow(B, 2)
        print("Сумма числ: ", Sum, "\nРізниця числ: ", Riz, "\nДобуток: ", Dob, "\nЧастка квадратів: ", CHkv)
    if(Number == 7):
        #За довжинами двох сторін деякого трикутника і кутом між ними знайти довжину третьої сторони і площу цього трикутника.
