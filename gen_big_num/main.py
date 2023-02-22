import random

from bbs import *
from prime import *

"""
Функция generate_prime() использует алгоритм BBS для генерации случайного числа,
а затем проверяет его с помощью теста на простоту Ферма и функции is_prime(), 
которая сверяет число со списком простых чисел, а затем использует пробное деление для любого большего числа.

Алгоритм BBS генерирует псевдослучайное число на основе начального начального значения, 
алгоритм использует квадратичный остаток для генерации числа, он детерминирован и требует относительно большого начального значения,
чтобы избежать шаблонов в сгенерированной последовательности.

Тест Ферма на простоту проверяет, является ли число n простым,
используя уравнение a ^ (n-1) ≡ 1 mod n для некоторого случайно выбранного a,
если уравнение справедливо для нескольких случайных as, то, вероятно, n является простым.
Тест может давать ложноположительные результаты для составных чисел, называемых "числами Кармайкла", которые встречаются очень редко.

Функция is_prime() использует список простых чисел, чтобы быстро проверить,
является ли число простым или нет, если число делится на любое из простых чисел в списке,
оно не простое, в противном случае используется пробное деление до квадратного корня из числа.

В целом, реализация относительно проста и быстра для генерации простых чисел, 
но ее корректность не гарантируется во всех случаях, поскольку она может давать ложные срабатывания и полагается на фиксированный список простых чисел. 
Более надежная реализация должна использовать вероятностные алгоритмы, такие как Miller-Rabin, или детерминированные алгоритмы, такие как AKS или доказа
"""


def is_prime(n: int) -> bool:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251]
    if n in primes:
        return True
    for prime in primes:
        if n % prime == 0:
            return False
    return True


def generate_prime(length: int, test_iterations: int):
    if length < 3:
        raise ValueError('length must be more then 2')

    random_numbers = bbs(11, 19, length - 2)

    result = 1 << (length - 1)

    d = length - 1
    for bit in random_numbers.values():
        result |= bit << d
        d -= 1
    result |= 1

    is_composite, percent = fermat_is_composite(result, test_iterations)
    print(
        f'Тест Ферма - число {result}:',
        'составное' if is_composite else f'возможно простое с вероятностью {percent}',
    )

    while not is_prime(result) or is_composite:
        result += 2
        result %= int(math.pow(2, length) + math.pow(2, length - 1))
        is_composite, percent = fermat_is_composite(result, test_iterations)
        print(
            f'Тест Ферма - число {result}:',
            'составное' if is_composite else f'возможно простое с вероятностью {percent}',
        )

    return result


def fermat_is_composite(n: int, iterations: int) -> (bool, float):
    if n <= 3 or not n % 2:
        raise ValueError('n should be an odd positive integer greater then 3')
    for _ in range(iterations):
        a = random.randrange(2, n - 2)
        if math.gcd(a, n) != 1:
            return True, 0
        t = pow(a, n - 1, n)
        if t != 1:
            return True, 0
    return False, (1 - (1 / (2 ** iterations))) * 100


if __name__ == '__main__':
    n = 20
    prime = generate_prime(n, 100)
    print(f'Простое число [{n} бит(a)]:', prime)
