def factorial(n):
    i = 1
    result = 1
    while i <= n:
        result *= i
        i += 1
    return result

x = factorial(10)
print("10! = " + str(x))
