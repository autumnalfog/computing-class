import time

def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n - 1) + fibo(n - 2)

def fibo_eff(n):
    a = 1
    b = 0
    iteration = 1
    while iteration < n:
        result = a + b
        b = a
        a = result
        iteration += 1
    return result 

def compare_functions(f, g, arg):
    i = 0
    t1 = 0
    t2 = 0
    while i < 1000:
        last_time = time.clock()
        f(arg)
        t1 += time.clock() - last_time
        last_time = time.clock()
        g(arg)
        t2 += time.clock() - last_time
        i += 1
    print(t2 / t1)
