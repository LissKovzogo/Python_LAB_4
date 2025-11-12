#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    a = list(map(int, input().split()))
    sum_a = 0
    count_a = 0
    for i in a:
        if (i < 0) and (i % 7 == 0):
            count_a += 1
            sum_a += i

    print(f"Количество = {count_a}\n Сумма = {sum_a}")