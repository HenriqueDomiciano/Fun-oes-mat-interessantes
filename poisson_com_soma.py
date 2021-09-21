import numpy as np 
import matplotlib.pyplot as plt
import math

def factorial(n):
    m = 1
    for r in range(n, 1, -1):
        m *= r
    return m

def poisson_func(lamb,y):
    return (math.e**(-lamb))*(lamb**y)/factorial(y)    

l=float(input('digite o lambda'))
d=int(input('digite o número de amostras (Para o gráfico) os limites devem estar entre este numero de amostras'))

x=[d for d in range(0,d+1)]
y=[poisson_func(l,i) for i in x]

inf=int(input("digite o limite inferior"))
sup=int(input("Digite o limite superior"))
res=0
for r in range(inf,sup+1):
    res+=y[r]
print(res)
'''
plt.figure('Poisson')
plt.scatter(x,y)
plt.show()
'''