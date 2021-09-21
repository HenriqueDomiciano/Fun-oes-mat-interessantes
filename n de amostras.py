import scipy.integrate as integrate
import scipy.stats


alpha=float(input("Digite o alpha do intervalo de confiança"))
ci = scipy.stats.norm.interval(alpha, loc=1, scale=1)
print(c)