#!/usr/bin/env python3
"""
Counting Sundays
 
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# дни недели
week = {
    0: 'ВС',
    1: 'ПН',
    2: 'ВТ',
    3: 'СР',
    4: 'ЧТ',
    5: 'ПТ',
    6: 'СБ',       
}

# количество дней в месяцах в обычном году
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(year):
    """
    это високосный год?
    """
    if year % 4 != 0:
        return False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return True

# 1900-01-01 Пн
# 1901-01-01 ВТ

# test of leap year
#for year in range(1900, 2023):
    #print(year, leap_year(year))

wd = 2
summ = 0
current_day = 0

def year_month(year, month):
    """
    Если месяц перешёл в новый год, то увеличить год на единицу и вычесть 12 из месяца
    с учетом нумерации с ноля и особенности начала подсчета добавить 2 для вывода
    """
    if month >= 11:
        return year + 1, month - 12 + 2
    return year, month + 2

for year in range(1901, 2001):
    d = 1 if leap_year(year) else 0
    for month in range(12):
        added = d if month == 1 else 0
        current_day += month_days[month] + added
        week_day = (2 + current_day) % 7
        y, m = year_month(year, month)
        if week_day == 0:
            summ += 1
            print(f'{y:4d}-{m:02d}-01 Воскресенье')

print(f'В 20 веке (1901-2000гг) {summ} раз первый день месяца приходился на воскресенье')
