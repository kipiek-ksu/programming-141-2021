
"""17. Дано ціле число N (> 1). Знайти найменше ціле число K, при якому виконується нерівність 3K> N.
"""
n = int(input('Введить число: '))
k = 0
if n <= 1:
    print('Введене число невірне')
while 3 * k <= n:
    k += 1
    print("найменше ціле число K, при якому виконується нерівність 3K> N = " + str(k))

