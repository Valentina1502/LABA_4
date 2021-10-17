#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit

code1 = '''
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''

code2 = '''
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''

code3 = '''
def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
        return product
'''

code4 = '''
def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
'''

code5 = '''
from functools import lru_cache
@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''
code6 = '''
from functools import lru_cache
@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''
if __name__ == '__main__':
    print('\nРезультат рекурсивго факториала: ', min(timeit.Timer(setup=code1).repeat(4, 1000)))
    print('Результат рекурсивного числа Фибоначчи:', min(timeit.Timer(setup=code2).repeat(4, 1000)))
    print('*    ' * 15)
    print('Результат итеративного факториала:', min(timeit.Timer(setup=code3).repeat(4, 1000)))
    print('Результат итеративного числа Фибоначчи:', min(timeit.Timer(setup=code4).repeat(4, 1000)))
    print('*    ' * 15)
    print('Результат факториала с декоратором:', min(timeit.Timer(setup=code5).repeat(4, 1000)))
    print('Результат числа Фибоначчи с декоратором:', min(timeit.Timer(setup=code6).repeat(4, 1000)))
