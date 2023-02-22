# Define the moduli and residues to be used in the RNS representation
moduli = [17, 19, 23]
residues = [2, 3, 4]


# функция для выполнения добавления RNS
def rns_add(a, b):
    # сумма остатков по модулю каждого модуля
    result = [(a[i] + b[i]) % moduli[i] for i in range(len(moduli))]
    return result


# функция для выполнения умножения RNS
def rns_multiply(a, b):
    # произведение остатков по модулю каждого модуля
    result = [(a[i] * b[i]) % moduli[i] for i in range(len(moduli))]
    return result


# Модульное сокращение
def rns_reduce(a):
    # коэффициенты китайской теоремы об остатках
    M = 1
    Mi = [0] * len(moduli)
    for i in range(len(moduli)):
        M *= moduli[i]
    for i in range(len(moduli)):
        Mi[i] = M // moduli[i]

    # Вычислите остаток от числа RNS по модулю M
    result = sum([(a[i] * Mi[i] * residues[i]) % M for i in range(len(moduli))]) % M
    return result


# Example 1: Perform RNS addition
a = [5, 7, 12]
b = [10, 12, 15]
print("RNS Addition Example:")
print("a =", a)
print("b =", b)
c = rns_add(a, b)
print("c =", c)

# Example 2: Perform RNS multiplication and reduction
a = [6, 8, 10]
b = [3, 5, 7]
print("RNS Multiplication and Reduction Example:")
print("a =", a)
print("b =", b)
c = rns_multiply(a, b)
print("c =", c)
d = rns_reduce(c)
print("d =", d)