import scipy.integrate as integrate
import scipy.stats

def t(x,df,mu,gamma):
    return scipy.stats.t.pdf(x,df,loc=mu,scale=gamma)

mu = float(input("Digite o Mu"))
selec= int(input("digite 1 para integral e o para probabilidade"))
df = int(input("digite o grau de liberdade"))

if selec:
    gamma = float(input("Digite o S")) 

    df = int(input("digite o grau de liberdade"))

    inferior = float(input("Digite o limite inferior"))

    superior = float(input("digite o limite superior"))

    res = integrate.quad(t,inferior,superior,args=(df,mu,gamma))[0]

    print(f'O resultado é : {res}')

    alpha= float(input("Digite o Alpha"))

    res = scipy.stats.t.interval(alpha,df,loc=mu,scale=gamma)

    print(f'O intervalo de confiança é : {res}')
else:
    x=float(input('Digite a probabilidade'))
    res= scipy.stats.t(df,loc=mu).ppf(x)
    print(f'O resultado é : {res}')