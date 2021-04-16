"""Дано дійсне число ε (> 0). Послідовність дійсних чисел AK визначається наступним чином:A1 = 1,
A2 = 2, AK = (AK-2 + 2 • AK-1) / 3, K = 3, 4, ....Знайти перший з номерів K, для яких виконується умова |
AK - AK-1 | <Ε, і вивести цей номер, а також числа AK-1 і AK"""
n = int(input('Введите число n'))
a1 = 1
a2 = 2
a3 = 3
for i in range(4, n + 1):
    a = a3
    a3 = a3 + a2 - 2 * a1
    a1 = a2
    a2 = a
    print(a3)
