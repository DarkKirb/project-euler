#!/usr/bin/env python3
# cython: language_level=3
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?


def isLeapYear(n):
    if not n % 400:
        return True
    if not n % 100:
        return False
    if not n % 4:
        return True
    return False


def getDayPerMonth(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if isLeapYear(year):
        return 29
    return 28


def getNoDays(day, month, year):
    if not day or day > getDayPerMonth(month, year):
        raise Exception
    if not month or month > 12:
        raise Exception
    days = day - 1
    days += sum((getDayPerMonth(m, year) for m in range(1, month)))
    days += sum(((366 if isLeapYear(y) else 365) for y in range(1900, year)))
    return days
getWeekDay = lambda day, month, year: getNoDays(
    day, month, year) % 7  # European calendar. starts with monday
count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if getWeekDay(1, month, year) == 6:
            count += 1
print(count)
