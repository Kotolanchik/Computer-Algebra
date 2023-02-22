import random
from math import gcd

"""
Этот код реализует алгоритм факторизации Полларда p-1. Учитывая составное число n и количество итераций iterations,
алгоритм генерирует последовательность чисел X с использованием функции f. Затем для каждой итерации он вычисляет наибольший общий делитель всех пар разностей между числами в последовательности до этой итерации, используя функцию gcd. Если наибольший общий делитель является собственным делителем n, он возвращает разложение n на множители как [curr_gcd, n // curr_gcd].

Функция f принимает число x и модуль n и возвращает (x^2 + 1) mod n.

Алгоритм использует модуль random для генерации случайного начального номера для последовательности.
"""


def f(x: int, n: int) -> int:
    return int(x * x + 1) % n


def p_pollard(n: int, iterations: int) -> list:
    if n < 9:
        raise ValueError('n must be greater then 8')

    X = [random.randint(2, 10)]
    for i in range(1, iterations + 2):
        X.append(f(X[i - 1], n))

    for i in range(iterations):
        for k in range(1, i + 2):
            for j in range(i + 1):
                curr_gcd = gcd(abs(X[j] - X[k]), n)
                if 1 < curr_gcd < n:
                    return [curr_gcd, n // curr_gcd]

    return [1, n]
