def fibo(n):
    print("Starting to compute " + str(n) + " Fibonacci number.")
    if n == 0: return 0
    if n == 1: return 1
    result = fibo(n - 1) + fibo(n - 2)
    print("Have computed " + str(n) + " Fibonacci number.")
    return result

saved_value = 0

def fiboe(n):
    global saved_value
    if n == 0: return 0
    if n == 1:
        saved_value = 0
        return 1
    result = fibo(n - 1) + saved_value
    saved_value = fibo(n - 1)
    return result
