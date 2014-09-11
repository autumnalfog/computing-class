def fibo(n):
    print("Starting to compute " + str(n) + " Fibonacci number.")
    if n == 0: return 0
    if n == 1: return 1
    result = fibo(n - 1) + fibo(n - 2)
    print("Have computed " + str(n) + " Fibonacci number.")
    return result