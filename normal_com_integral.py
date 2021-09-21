import numpy as np
import matplotlib.pyplot as plt 
import math
import scipy.integrate as integrate
import scipy.stats

def normal(x,mu,sigma):
    return (1/(sigma*((2*math.pi)**0.5)))*(math.e**(-0.5*(((x-mu)/sigma)**2)))

n_of_points=1000
mu=float(input('Digite a média'))
sigma=float(input("digite o sigma"))
#limit=float(input('digite o limite(grafico)'))
#res=float(input('digite o valor do ponto que deseja saber'))

#x=np.linspace(-limit,limit,n_of_points)
#y=[normal(i,mu,sigma) for i in x]
if int(input('Digite 0 para ppf e 1 para pdf com Integral'))==1:
    inf=float(input('Digite o limite inferior'))
    sup=float(input("Digite o limite superior"))
    res=integrate.quad(normal,inf,sup,args=(mu,sigma))

    print(f'O resultado da integral é {res[0]} ')

    alpha=float(input("Digite o alpha do intervalo de confiança"))
    ci = scipy.stats.norm.interval(alpha, loc=mu, scale=sigma)
    print(ci)
else:
    print(scipy.stats.norm(mu,sigma).ppf(float(input('Digite a probabilidade'))))

'''
plt.figure("Normal")

plt.plot(x,y)

plt.show()
'''