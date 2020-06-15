# -*- coding:utf-8 -*-

#%%
import numpy as np
import pandas as pd
import datetime as dt

import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter


'''
# <<<<<<<<<<<<<<<<<<Gauss Ditribution<<<<<<<<<<<<<<<<<<
#%%
mu = 0
sigma  = 1

X = np.linspace(-3 * sigma,  3 * sigma,  1000)

guass = lambda x: np.sqrt(2 * np.pi * 2) * sigma * np.e ** (-(x - mu) ** 2 / (2 * sigma ** 2))
Y = guass(X)
plt.scatter(X, Y, s=1)
plt.show()


#%%
n = np.random.normal(loc=0.0,  scale=0.2,  size=10000)
plt.hist(n, bins=100)
plt.show()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''


'''
# <<<<<<<<<<<<<<<<Poisson Distribution<<<<<<<<<<<<<<<<<
#%%
import math

lam = 10
X = pd.Series(np.arange(0, 50))

poisson = lambda x: (lam ** x) * np.e ** (-lam) / math.factorial(x)
Y = X.apply(poisson)
plt.plot(X,  Y)
plt.show()


#%%
n = pd.Series(np.random.poisson(5, 10000))
plt.hist(n,  bins=100)
plt.show()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''


# <<<<<<<<<<<<<<<<Binormial Distribution<<<<<<<<<<<<<<<<<
#%%
import math

# 实验次数
n = 1000;
# 抽到次数
X = pd.Series(np.arange(0, 100))
# 单次概率
p = 0.03


f = math.factorial
binormial = lambda x: f(n) / (f(x) * f(n - x)) * (p**x) * (1 - p)**(n - x)
Y = X.apply(binormial)

plt.plot(X, Y)
plt.show()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
