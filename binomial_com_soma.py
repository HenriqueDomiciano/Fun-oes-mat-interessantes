import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def factorial(n):
    m = 1
    for r in range(n, 1, -1):
        m *= r
    return m


def binomial_dist(n, k, p):
    return ((factorial(n))/(factorial(n-k)*factorial(k)))*(p**k)*(p-1)**(n-k)


n = int(input("digite o numero de amostras" ))
p = float(input("digite o valor de probabilidade"))

k = [abs(binomial_dist(n, i, p)) for i in range(0, n+1)]


x = np.linspace(0, n, n+1)

y=[[x[i],k[i]] for i in range(len(k))]

resu=0
s=int(input("digite o menor limite"))
p=int(input('digite o limite maior'))
for r in range(s,p+1):
    resu+=k[r]

print(resu)

plt.figure(0)
plt.scatter(x, k, marker='*')
''
#plt.plot(x, k)
#plt.plot(x1, k1)

plt.show()
