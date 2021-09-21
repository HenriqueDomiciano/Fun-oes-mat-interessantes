import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def soma_a_direita(a,b,deltax,f):
    valores = []
    n = int(abs(a-b)/deltax)
    for i in range(1,n+1):
        valores.append(f(a+i*deltax))
    return deltax*sum(valores),valores

def soma_a_esquerda(a,b,deltax,f):
    valores = []
    n = int(abs(a-b)/deltax)
    for i in range(n):
        valores.append(f(a+i*deltax))
    return deltax*sum(valores),valores

def soma_media(a,b,deltax,f):
    valores = []
    n = int(abs(a-b)/deltax)
    for i in range(n):
        valores.append(f(a+(i*deltax+(deltax/2))))
    return deltax*sum(valores),valores

f= lambda x: x
g = lambda x : 1
h = lambda x: 1*(x-2.5)**2
k = lambda x: 1
l = lambda x : -x+5
lista_de_funcoes = [f,g,h,k,l]
soma = 0 
pontos = []
soma_real = 0 
deltax = float(input('Digite o valor de dx'))
x= np.arange(0,5+deltax,deltax)
lista_de_intervalo=[(0,1),(1,1.5),(1.5,3.5),(3.5,4),(4,5)]
plt.figure(figsize=(12,6))
for i in range(len(lista_de_funcoes)):
    intervalo = lista_de_intervalo[i]
    inter_parc= np.arange(intervalo[0],intervalo[1]+0.01,0.01)
    plt.plot(inter_parc,[lista_de_funcoes[i](k) for k in inter_parc],color='r')
    res = soma_a_esquerda(intervalo[0],intervalo[1],deltax,lista_de_funcoes[i])
    soma+= res[0]
    pontos.append(res[1])
    soma_real += quad(lista_de_funcoes[i],intervalo[0],intervalo[1])[0]
print(soma,soma_real)
plt.title(f"Error is {100*abs(round((soma_real-soma)/soma_real,3))}% resultcalc:{soma}")
plt.xlabel("X")
plt.ylabel("Y")
pontos = [item for sublist in pontos for item in sublist]
for i in range(1,len(pontos)):
    plt.fill_between([x[i-1],x[i]],pontos[i-1],0,color='b')
    
plt.show()