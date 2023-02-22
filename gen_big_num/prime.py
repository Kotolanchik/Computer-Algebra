import math

"""
Функция eratosthenes_sieve реализует алгоритм сита Эратосфена для нахождения всех простых чисел с точностью до заданного числа n.
 Он начинается с создания набора списков с чередующимися значениями 1 и 0, представляющими нечетные и четные числа соответственно.
  Затем он перебирает все нечетные числа от 3 до n, и для каждого числа он пропускает итерацию, если оно четное, а если оно нечетное,
   он помечает все кратные этому числу как составные, устанавливая соответствующий индекс в set равным 0. Наконец,
    он создает результат списка со всеми простыми числами, которые являются индексами набора, имеющими значение 1.

Функция lucas_criterion реализует тест на примитивность Lucas. 
Он начинается с нахождения всех простых делителей n-1 с помощью вспомогательной функции __prime_divisors, 
а затем перебирает диапазон целых чисел a от 2 до итераций. Для каждого a и каждого простого делителя q он проверяет,
 является ли a ^ (n-1) = 1 mod n и a ^ ((n-1)/q) ! = 1 mod n. Если оба условия выполняются для некоторых a и q, это возвращает True,
  указывая, что n, вероятно, простое число. Если такие a и q не найдены, он возвращает False.

Функция __prime_divisors использует функцию eratosthenes_sieve для нахождения всех простых чисел вплоть до заданного числа n, 
а затем проверяет, какие из этих простых чисел делят n.

Функция test_divisions - это простой тест на примитивность, который проверяет,
 делится ли n на любое целое число от 2 до квадратного корня из n. Если такое целое число не найдено, оно возвращает значение True,
  указывающее, что n является простым числом.
"""


def eratosthenes_sieve(n: int) -> list:
    set = [1]
    for i in range(3, n + 1):
        set.append(0 if i % 2 == 0 else 1)

    for i in range(3, math.ceil(math.sqrt(n)) + 1):
        current = i
        if set[i - 2] == 0:
            continue
        for j in range(i + 1, n + 1):
            if set[j - 2] == 0:
                continue
            if j % current == 0:
                set[j - 2] = 0

    result = []
    for i in range(len(set)):
        if set[i] == 0:
            continue
        result.append(i + 2)

    return result


def lucas_criterion(n: int, iterations: int) -> bool:
    qs = __prime_divisors(n - 1)

    for a in range(2, iterations + 1):
        for q in qs:
            if pow(a, n - 1) % n == 1 and pow(a, int((n - 1) / q)) % n != 1:
                return True

    return False


def __prime_divisors(n: int) -> list:
    result = []
    for prime in eratosthenes_sieve(n):
        if n % prime == 0:
            result.append(prime)
    return result


def test_divisions(n: int) -> bool:
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
