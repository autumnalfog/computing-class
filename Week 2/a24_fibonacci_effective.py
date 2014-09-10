def fibo(n):
    a = 1
    b = 0
    iteration = 1
    while iteration < n:
        result = a + b
        b = a
        a = result
        iteration += 1
    return result 
              
        
