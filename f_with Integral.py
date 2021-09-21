import scipy.integrate as integrate
import scipy.stats

def f(x,dfn,dfd):
    return scipy.stats.f.pdf(x,dfn,dfd)



dfn = int(input("digite o  primeiro grau de liberdade"))

dfd= int(input("digite o segundo grau de liberdade"))

selec=int(input("digite 0 para pmf e 1 para integral"))
if selec==1:
    inferior= float(input("Digite o limite inferior"))

    superior=float(input("digite o limite superior"))
    res=integrate.quad(f,inferior,superior,args=(dfn,dfd))[0]
else : 
    x=float(input('Digite a probabilidade'))
    res= scipy.stats.f(dfn,dfd).ppf(x)
print(f'O resultado é : {res}')
