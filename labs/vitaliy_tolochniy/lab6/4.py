"""Лабораторная работа 6
Толочный Виталий 141
Описати функцію Cos1 (x, ε) дійсного типу (параметри x, ε - дійсні, ε> 0),
знаходить наближене значення функції cos (x):
cos (x) = 1 - x2/ (2!) + x4/ (4!) - ... + (-1) n· x2 · n / ((2 · n)!) + ....
В сумі враховувати всі складові, модуль яких більше ε. За допомогою Cos1
знайти наближене значення косинуса для даного x при шести даних ε. """

def Cos1(x, e):
    s = 1
    symbol = 1
    n = 2
    skl = x ** 2/2
    while(skl>e):
        s+=(skl * symbol)
        symbol *= -1
        skl = skl * (x ** 2/((2 + n) * (1 + n)))
        n += 2
    return s

x = float(input("Введите x: "))
l1 = [float(i) for i in input("Введите ε: ").split()]
for i in l1:
    print(round(Cos1(x,i),2))
