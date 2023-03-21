import numpy as np
from matplotlib import pyplot as plt

seed = 453
np.random.seed(seed)
p0 = 1/2
p1 = 1/(1 + np.sqrt(5))
p2 = (3 - np.sqrt(5))/4
z_values = []

def my_plot_init():
    axes = plt.axes()
    [axx.set_linewidth(0.2) for axx in axes.spines.values()]
    axes.margins(x=0)
    axes.margins(y=0)
    axes.tick_params(axis='both', which='major', labelsize=7)
    axes.tick_params(axis='both', which='minor', labelsize=7)
    return()

for number in range(1000000):
    z = 0.0
    prod = 1.0
    for k in range(60):
        rnd = np.random.rand()
        if rnd < p0:
            x_k = 0
        elif rnd < p0 + p1:
            x_k = 1
        else:
            x_k = 2
        z = np.sqrt(x_k + z)
    z_values.append(z)

x = np.sort(z_values)
y = np.arange(len(x))/float(len(x))
approx = []
for arg in x:
    val = np.log(arg)/np.log(2)
    approx.append(val) 

my_plot_init()
plt.plot(x, y, linewidth = 0.4)
plt.plot(x, approx, linewidth = 0.4)
plt.show()

my_plot_init()
plt.plot(x, y-approx, linewidth = 0.4)
plt.show()

