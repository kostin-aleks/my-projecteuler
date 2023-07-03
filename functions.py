"""
Набор полезных функций
"""

def int_to_en(num):
    """
    Given an int32 number, print it in English.
    """
    d = {
        0: 'zero', 
        1: 'one', 
        2: 'two', 
        3: 'three', 
        4: 'four', 
        5: 'five',
        6: 'six', 
        7: 'seven', 
        8: 'eight', 
        9: 'nine', 
        10: 'ten',
        11: 'eleven', 
        12: 'twelve', 
        13: 'thirteen', 
        14: 'fourteen',
        15: 'fifteen', 
        16: 'sixteen', 
        17: 'seventeen', 
        18: 'eighteen',
        19: 'nineteen', 
        20: 'twenty',
        30: 'thirty', 
        40: 'forty', 
        50: 'fifty', 
        60: 'sixty',
        70: 'seventy', 
        80: 'eighty', 
        90: 'ninety' 
    }
    
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]
    if (num < 100):
        if num % 10 == 0: 
            return d[num]
        else: 
            return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: 
            return d[num // 100] + ' hundred'
        else: 
            return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: 
            return int_to_en(num // k) + ' thousand'
        else: 
            return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: 
            return int_to_en(num // m) + ' million'
        else: 
            return int_to_en(num // m) + ' million, ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: 
            return int_to_en(num // b) + ' billion'
        else: 
            return int_to_en(num // b) + ' billion, ' + int_to_en(num % b)

    if (num % t == 0): 
        return int_to_en(num // t) + ' trillion'
    else: 
        return int_to_en(num // t) + ' trillion, ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))


def factorial(n):
    """
    calculates factorial for n
    """
    result = 1
    for m in range(2, n + 1):
        result *= m
    return result


def is_prime(number):
    """
    number is prime ?
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_prime_number(n):
    """
    function to find if the given
    number is prime
    """
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def eratosthenes2(n):
    """
    решето Эратосфена для простых чисел
    генератор
    """
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
