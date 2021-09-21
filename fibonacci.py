def fibonacci(n):
    m=0
    a=1
    b=1
    c=0
    while m<n:
        a=b+c
        c=b
        b=a
        m+=1
    return(c)
print(fibonacci(1000))