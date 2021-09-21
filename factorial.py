def factorial(n):
    m=1
    for r in range(n,1,-1):
        m*=r
    return m
print(factorial(1000))
