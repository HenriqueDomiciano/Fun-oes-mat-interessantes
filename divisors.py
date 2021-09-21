def divisors(n):
    d=[]
    for r in range(1,int(n**0.5)):
        if n%r==0:
            d.append(r)
            d.append(int(n/r))
    return sorted(d)
print(divisors(int(input('Digite o numero'))))