"""Дано змінні A,B,C.Змінити їх значення, перемістивши вміст А в В, В -в С-в А, ы вивести новы значення
змінних А,В,С """
A = int(input('Введіть число:'))
B = int(input('Введіть число:'))
C = int(input('Введіть число:'))
ta = A
tb = B
tc = C
B = ta
C = tb
A = tc
print(A)
print(B)
print(C)