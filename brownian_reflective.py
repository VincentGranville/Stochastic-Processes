import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF

m = 2000 
a = 0.5
b = 0.5
T = []
X = []
Z = []
T.append(0.0)
X.append(0.0)
Z.append(0.0)
np.random.seed(1979)
for k in range(1,m):
    u = np.random.uniform(0,1)
    u = u**b
    if X[k-1] < 0:
        X.append(X[k-1] + u/(k**a))
    else:
        X.append(X[k-1] - u/(k**a))
    Z.append((k**a) * X[k])
    T.append(T[k-1] + 1)
   
axes = plt.axes()
axes.tick_params(axis='both', which='major', labelsize=8)
axes.tick_params(axis='both', which='minor', labelsize=8)
for axis in ['top','bottom','left','right']:
    axes.spines[axis].set_linewidth(0.5) 
plt.plot(T, Z, linewidth = 0.4, color = 'green', alpha = 1)  
plt.axhline(y = 0.0, color = 'black', linestyle = '--', linewidth = 0.4)
plt.show()

ecdf = ECDF(Z[10:len(Z)])
sns.set_context("paper",font_scale=0.8, rc={"lines.linewidth": 0.8})
sns.displot(Z[10:len(Z)], kind="kde",linewidth=0.5) ### , bins=150)
plt.show()
