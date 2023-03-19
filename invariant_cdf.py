import numpy as np
from matplotlib import pyplot as plt

seed = 453
np.random.seed(seed)
p = 0.8
a = 0.4
b = 0.6
z_values = []

for number in range(10000):
    z = 0.0
    prod = 1.0
    for k in range(60):
        rnd = np.random.rand()
        if rnd < p:
            x_k = b
        else:
            x_k = a
        prod = prod * x_k
        z += prod
    z_values.append(z)

x = np.sort(z_values)
y = np.arange(len(x))/float(len(x))

axes = plt.axes()
[axx.set_linewidth(0.2) for axx in axes.spines.values()]
axes.margins(x=0)
axes.margins(y=0)
axes.tick_params(axis='both', which='major', labelsize=7)
axes.tick_params(axis='both', which='minor', labelsize=7)
plt.plot(x, y, linewidth = 0.4)
plt.show()
