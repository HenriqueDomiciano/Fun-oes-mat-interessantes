import scipy.integrate as integrate
import scipy.stats

def chi(x,df):
    return scipy.stats.chi2.ppf(x,df)

df = int(input("digite o grau de liberdade"))

selec=int(input('Digite 1 para integral e 0 para posicionamento em tabela'))

if selec:
    inferior= float(input("Digite o limite inferior"))
    
    superior=float(input("digite o limite super"))

    res=integrate.quad(chi,inferior,superior,args=(df))[0]
else:
    x= float(input('Digite a probabilidade'))

    res=scipy.stats.chi2(df).ppf(x)
    
print(f'O resultado é : {res}')
