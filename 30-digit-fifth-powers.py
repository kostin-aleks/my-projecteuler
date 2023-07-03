#!/usr/bin/env python3
"""
Digit fifth powers

Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

# Сумма пятых степеней цифр максимальна когда все цифры равны 9
# 1 цифра: 1 x 9^5 = 59049
# 2 цифры: 2 x 9^5 = 118098
# 3 цифры: 3 x 9^5 = 177147
# 4 цифры: 4 x 9^5 = 236196
# 5 цифр : 5 x 9^5 = 295245
# 6 цифр : 6 x 9^5 = 354294
# 7 цифр : 7 x 9^5 = 413343

# Интересна последняя строчка: невозможно, чтобы семизначное число было суммой пятых степеней его цифр.
# Потому что все суммы составляют максимум шестищначное число.

# Если мы проанализируем все числа от 2 до 354294 (максимальная сумма для 6 цифр), 
# то мы сможем решить задачу:
# 1. разделить число на цифры
# 2. сложить пятые степени этих цифр
# 3. если сумма равна числу, то добавляем число в результат

def is_perfect(n):
    """
    проверить, что сумма пятых степеней цифр числа
    рана самому числу
    """
    digits = [int(x) for x in str(n)]
    summ = sum([x ** 5 for x in digits])
    return summ == n

lst = []
for n in range(2, 354295):
    if is_perfect(n):
        lst.append(n)
        
print(f'all the numbers that can be written as the sum of fifth powers of their digits are {lst}.')
print(f'sum of these numbers is {sum(lst)}')
