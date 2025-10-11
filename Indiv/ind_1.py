#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    A = list(map(int, input().split()))
    sum_A = 0
    count_A = 0
    for i in A:
        if (i < 0) and (i % 7 == 0):
            count_A += 1
            sum_A += i

    print(f"Количество = {count_A}\n Сумма = {sum_A}")