# basins.py | find and plot basins of attraction of 2D sine map

import numpy as np
import matplotlib.pyplot as plt

llambda  = 2  
theta    = 1     
learning = 0.75
eps      = 0.00001
eps2     = 0.2

n_basins = 0
basin_count = {}
basin_color = {}
list_x = []
list_y = []
list_color = []

color = [(0, 0, 0),
         (1, 0, 0),
         (0, 0, 0), 
         (1, 0, 0), 
         (1, 1, 1), # (0.9, 0.8, 1)
         (1, 1, 0),
         (0, 0, 1), 
         (0, 1, 1)]

OUT=open("basins.txt","w")

for X_0 in np.arange(-4, 4, 0.01):
    print("X_0 =",X_0)
    for Y_0 in np.arange(-4, 4, 0.01):
        x = X_0
        y = Y_0
        k = 0
        delta = 999999.9
        for k in range(100): 
            old_x = x
            old_y = y
            x =(1-learning)*old_x + llambda*np.sin(theta*old_y)
            y =(1-learning)*old_y + llambda*np.sin(theta*old_x)
            delta = max(abs(x-old_x), abs(y-old_y))
        if abs(x)<eps:
            x = 0
        if abs(y)>eps:
            y = 0
        if delta>0.2: 
            basin_ID = -1   # non-convergence zone (oscillating) 
        else:
            basin_ID = int(100 + 10*x + y + 0.5)
        if basin_ID in basin_count:
            basin_count[basin_ID] += 1 
        else:
            basin_count[basin_ID] = 1
            n_basins = n_basins + 1
            basin_color[basin_ID] = color[n_basins]
        list_x.append(X_0)
        list_y.append(Y_0)
        list_color.append(basin_color[basin_ID])

OUT.close()

for basin_ID,count in basin_count.items():
    print(basin_ID, count, basin_color[basin_ID])

axes = plt.axes()
[axx.set_linewidth(0.2) for axx in axes.spines.values()]
# axes.set_facecolor("white")   # background color
axes.margins(x=0)
axes.margins(y=0)
axes.tick_params(axis='both', which='major', labelsize=7)
axes.tick_params(axis='both', which='minor', labelsize=7)
plt.scatter(list_x, list_y, c=list_color, s=0.1)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.show()
