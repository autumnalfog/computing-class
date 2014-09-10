def divide_while_aliquot(num, div):
    while num % div == 0:
        num //= div
    return num

def maximum_prime(n):
    if n == 1:
        return 1
    n = divide_while_aliquot(n, 2)
    if n == 1:
        return 2
    n = divide_while_aliquot(n, 3)
    if n == 1:
        return 3
    k = 1
    while True:
        divider = 3 * k - 1
        n = divide_while_aliquot(n, divider)
        if n == 1:
            return divider
        divider = 3 * k + 1
        n = divide_while_aliquot(n, divider)
        if n == 1:
            return divider
        k += 1
