#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    a =  list(map(int, input("Введите список: ").split()))
    s = int(input("Ведите нижнюю границу диапазона: "))
    b = int(input("Ведите верхнюю границу диапазона: "))

    min_a = min(a)
    max_a = max(a)
    ind = a.index(max_a)
    sum_a = 0

    if abs(min_a) > max_a:
        ind = a.index(min_a)

    ind_s = -1

    for i in a:
        if i > 0:
            ind_s = a.index(i)
            break

    sum_a  = sum(a[ind_s+1::])
    a = sorted(a, key=lambda x: (0 if s <= x <= b else 1, x))

    print("номер максимального по модулю элемента списка", ind)
    print("сумму элементов списка, расположенных после первого положительного элемента",sum_a)
    print(a)