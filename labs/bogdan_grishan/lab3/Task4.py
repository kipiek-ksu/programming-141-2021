"""
Дано ціле число N (> 0). Знайти квадрат даного числа, використовуючи для його обчислення
наступну формулу: N2 = 1 + 3 + 5 + ... + (2 • N - 1).
"""

N = int(input("Введите число:"))
Sum = 0
x = 1

if N < 0:
    print("Введено неверное значение")
while N >= x:
    Sum = Sum + (2 * x - 1)
    x += 1
print("Квадрат числа " + str(N) + " равно " + str(Sum))
