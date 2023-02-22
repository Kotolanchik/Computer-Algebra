from fermat import *
from sherman_leman import *
from p_pollard import *

if __name__ == '__main__':
    n = 14351

    print(f'Метод Ферма для числа {n}:', fermat(
        n,
    ))

    n = 1219

    print(f'Метод Шермана-Лемана для числа {n}:', sherman_leman(
        n,
    ))

    n = 713

    print(f'Метод p-Полларда для числа {n}:', p_pollard(
        n, 100
    ))
