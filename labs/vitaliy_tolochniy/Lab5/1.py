
Толочний Виталiй 141
Розробіть функції для здійснення наступних операцій зі списками:
1. Введення списку;
2. Заповнення списку випадковими числами;
3. Виведення списку;
4. Пошук елементу за значенням;
5. Пошук максимального елементу;
6. Сортування списку за зростанням (спаданням);


import random
import module

a = 0
listt = []
while (a != 8):
    a = int(input('''Выберите, что вы хотите сделать, и введите номер команды:
1. Введення списку;
2. Заповнення списку випадковими числами;
3. Виведення списку;
4. Пошук елементу за значенням;
5. Пошук максимального елементу;
6. Сортування списку за зростанням (спаданням);
7. Пошук середнього арифметичного;
8. Вихід
'''))

    if a == 1:
        listt = module.InputList()
    elif a == 2:
        b = int(input('Введите длину списка:'))
        listt = module.RandInt(b)
    elif a == 3:
        if len(listt) == 0:
            print("Вы еще не создали ни одного списка")
        else:
            module.OutputList(listt)
    elif a == 4:
        if len(listt) == 0:

            print("Вы еще не создали ни одного списка")
        else:
            el = input("Введите элемент, чтобы найти его индекс в списке:")
            c = module.FindAnElement(listt, el)
            if c == -1:
                print("В этом списке нет такого элемента")
            else:
                print(c)
    elif a == 5:
        if len(listt) == 0:
            print("Вы еще не создали ни одного списка")
        else:
            print(module.FindMax(listt))
    elif a == 6:
        if len(listt) == 0:
            print("Вы еще не создали ни одного списка")
        else:
            reverse = bool(input("Вы хотите, чтобы ваш список был перевернут? Введите 'True' или 'False':"))
            listt = module.SortList(listt, reverse)
    elif a == 7:
        if len(listt) == 0:
            print("Вы еще не создали ни одного списка")
        else:
            print(module.Averege(listt))
    elif a == 8:
        print("До новых встреч)")
    else:
        print("Введите корректное число!")

