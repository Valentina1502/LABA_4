#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list_sum(list2):
    """
    возвращает сумму элементов входящего списка
    Вытаскиваетеся первый элемент из списка с помощью
    среза и передается в следующий рекурсивный вызов функции
    """
    if list2 == []:
        return 0
    else:
        summ = list_sum(list2[1:])
        summ = summ + list2[0]
        return summ


def list1():
    """
    Поэлементный ввод значений в список
    возвращает список элементов
    """
    numbers = []
    print("Введите элементы (до 7) списка через Enter\n"
          "Отрицательное число - признак конца ввода")
    for i in range(7):
        element = int(input())
        if element > 0:
            numbers.append(element)
        else:
            break
    return numbers


if __name__ == '__main__':

    p = list1()
    print('Список: ', p)
    print('Длина списка: ', len(p))
    print('Сумма элементов списка: ', list_sum(p))
