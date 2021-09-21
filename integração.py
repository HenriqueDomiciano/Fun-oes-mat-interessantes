from scipy.integrate import quad
print(f'{quad(lambda x : 2*x,1,4)[0]} o erro foi de {quad(lambda x : 2*x,1,4)[1]}')