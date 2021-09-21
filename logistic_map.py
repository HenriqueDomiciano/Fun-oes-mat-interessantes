import matplotlib.pyplot as plt
from matplotlib import style
it=[]
res=float(input("digite o valor de lambda"))
y=float(input("digite o valor inicial"))
iterations=int(input("digite o numero de iteraçoes"))
x=[i for i in range(iterations)]
for r in range(iterations):
    y=res*y*(1-y)
    it.append(y)

plt.figure(0)
style.use('bmh')
plt.plot(x,it)
plt.show()
