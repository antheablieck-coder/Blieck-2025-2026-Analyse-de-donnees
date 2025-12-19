#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats
import matplotlib.pyplot as plt

#https://docs.scipy.org/doc/scipy/reference/stats.html


dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']

print(dist_names)

#Loi de Dirac
centre=1
x=[0,1,2,3,4,5]
Dirac=scipy.stats.rv_discrete(values=([centre],[1]))
y=Dirac.pmf(x)
plt.figure()
plt.title ("Loi de Dirac centrée en 1")
plt.bar(x,y)
plt.xlabel ("valeur")
plt.ylabel ("probabilité")
#plt.show()
plt.close()
print ("DIRAC Moyenne:",Dirac.mean(),"Ecart type:",Dirac.std())

#Loi uniforme discrète
distribution=scipy.stats.randint(0,6)
plt.figure()
plt.stem(x,distribution.pmf(x))
plt.title ("Loi uniforme discrète")
plt.xlabel ("valeur")
plt.ylabel ("probabilité")
#plt.show()
plt.close()
print ("UNIFORME DISCRETE Moyenne:",distribution.mean(),"Ecart type:",distribution.std())

#Loi binomiale
distribution=scipy.stats.binom(6,0.4)
plt.figure()
plt.stem(x,distribution.pmf(x))
plt.title ("Loi binomiale")
plt.xlabel("valeur")
plt.ylabel("probabilité")
#plt.show()
plt.close()
print ("BINOMIALE Moyenne:",distribution.mean(),"Ecart type:",distribution.std())

#Loi de Poisson
distribution=scipy.stats.poisson(4)
plt.figure()
plt.stem(x,distribution.pmf(x))
plt.title ("Loi de Poisson")
plt.xlabel("valeur")
plt.ylabel("probabilité")
#plt.show()
plt.close()
print ("POISSON Moyenne:",distribution.mean(),"Ecart type:",distribution.std())

#Loi de Zipf-Mandelbrot
distribution=scipy.stats.zipf(2)
plt.figure()
plt.stem(x,distribution.pmf(x))
plt.title ("Loi de Zipf-Mandelbrot")
plt.xlabel("valeur")
plt.ylabel("probabilité")
#plt.show()
plt.close()
print ("ZIPF-MANDELBROT Moyenne:",distribution.mean(),"Ecart type:",distribution.std())

#Loi de Poisson continue (exponentielle)
x=np.linspace(0,10,500)
p=scipy.stats.expon.pdf(x)
plt.figure()
plt.plot(x,p)
plt.title("Loi de Poisson continue")
plt.xlabel("valeur")
plt.ylabel("probabilité")
#plt.show()
plt.close()
dist=scipy.stats.expon(scale=1/3)
print ("POISSON CONTINUE Moyenne:",dist.mean(),"Ecart type:",dist.std())

#Loi normale
moyenne=0
ecart=1
x=np.linspace(moyenne-4*ecart,moyenne+4*ecart,500)
p=scipy.stats.norm.pdf(x,loc=moyenne,scale=ecart)
plt.figure()
plt.plot(x,p,label=f"N({moyenne},{ecart**2})")
plt.title("Loi normale")
plt.xlabel("valeur")
plt.ylabel("probabilité")
#plt.show()
plt.close()
dist=scipy.stats.norm(loc=moyenne,scale=ecart)
print ("NORMALE Moyenne:",dist.mean(),"Ecart type:",dist.std())

#Loi log-normale
moyenne=0
ecart=0.5
x=np.linspace(0.001,5,500)
p=scipy.stats.lognorm(s=ecart,scale=np.exp(moyenne)).pdf(x)
plt.figure()
plt.plot(x,p,label=f"LogNorm(mu={moyenne},sigma={ecart})")
plt.title("Loi log-normale")
plt.xlabel("valeur")
plt.ylabel("probabilité")
#plt.show()
plt.close()
dist=scipy.stats.lognorm(s=ecart,scale=np.exp(moyenne))
print ("LOGNORMALE Moyenne:",dist.mean(),"Ecart type:",dist.std())

#Loi uniforme
inf=2
sup=6
x=np.linspace(inf-1,sup+1,500)
p=scipy.stats.uniform(loc=inf,scale=sup-inf).pdf(x)
plt.figure()
plt.plot(x,p,label=f"Uniforme({inf},{sup})")
plt.title("Loi uniforme")
plt.xlabel("valeur")
plt.ylabel("probabilité")
#plt.show()
plt.close()
dist=scipy.stats.uniform(loc=inf,scale=sup-inf)
print ("UNIFORME Moyenne:",dist.mean(),"Ecart type:",dist.std())

#Loi du X²
k=4
x=np.linspace(0,20,500)
p=scipy.stats.chi2(df=k).pdf(x)
plt.figure()
plt.plot(x,p,label=f"Chi²(k={k})")
plt.title("Loi du X²")
plt.xlabel("valeur")
plt.ylabel("probabilité")
#plt.show()
plt.close()
dist=scipy.stats.chi2(df=k)
print ("X² Moyenne:",dist.mean(),"Ecart type:",dist.std())

#Loi de Pareto
forme=3
scale=1
x=np.linspace(scale,10,500)
p=scipy.stats.pareto(b=forme,scale=scale).pdf(x)
plt.figure()
plt.plot(x,p,label=f"Pareto(alpha={forme},xm={scale})")
plt.title("Loi de Pareto")
plt.xlabel("valeur")
plt.ylabel("probabilité")
#plt.show()
plt.close()
dist=scipy.stats.pareto(b=forme,scale=scale)
print ("PARETO Moyenne:",dist.mean(),"Ecart type:",dist.std())



