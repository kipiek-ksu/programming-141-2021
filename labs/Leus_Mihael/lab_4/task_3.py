"""
lab4_z3
"""

"""
9. Дано рядок, що містить принаймні один символ пробілу. Вивести підрядок, розташований між
першим і останнім пробілом початкового рядка. Якщо рядок містить тільки один пробіл, то вивести
порожний рядок.
"""

s = 'bxjdididi zzzzzzzz ududhsh'
a = s.find(' ')
b = s.rfind(' ')
print (s[a:b])