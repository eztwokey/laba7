#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 5
# Ввести список А из 10 элементов, найти сумму элементов, больших 3 и меньших 8 и
# вывести ее на экран.
import sys

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    s = 0
    for item in A:
        if item > 3 and item < 8:
            s += item
    print(s)
