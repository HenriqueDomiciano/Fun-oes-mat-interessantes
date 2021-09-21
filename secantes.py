import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')
f = lambda x: x**6-x-1
ax.grid()
x0 = float(input('Digite o ponto a'))
x1 = float(input('Digite o ponto b'))
n = int(input('digite o número de iterações'))
m = np.linspace(1,2,100)
ax.plot(m,f(m))
x=[x0,x1]
y = [f(x0),f(x1)]
def init() :
    return ln

def animate(i):
    
    x1 = ((x[-2]*f(x[-1]))-(x[-1]*f(x[-2])))/(f(x[-1])-f(x[-2]))
    x.append(x1)
    y.append(f(x1))
    ax.plot(x[-2:],y[-2:])

    return ln,
ani = FuncAnimation(fig, animate, frames=np.linspace(0, n, n ),
                    init_func=init,interval= 1000)
plt.show()
print(x[-1])