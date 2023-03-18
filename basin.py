# basins.py | find and plot basins of attraction of 2D sine map

import numpy as np
import matplotlib.pyplot as plt

llambda  = 2 
theta    = 1     
rho      = -0.25  # rho replaced by c-1 in older version   
eps      = 0.00001

n_basins = 0
basin_count = {}
basin_color = {}
basin_x     = {}
basin_y     = {}
list_x = []
list_y = []
list_color = []

seed = 102 
np.random.seed()

# first 10 colors are pre-set
color = []
color= [(0.0, 1.0, 0.0),
        (1.0, 0.0, 1.0),
        (0.0, 0.0, 0.0), 
        (1.0, 0.0, 0.0), 
        (1.0, 1.0, 1.0), 
        (1.0, 1.0, 0.0), 
        (0.0, 0.0, 1.0), 
        (0.5, 0.5, 0.0),
        (0.0, 0.0, 0.7), 
        (0.0, 0.6, 0.3)
       ] 
n_cols   = 10

OUT=open("basins.txt","w")

for X_0 in np.arange(-4, 4, 0.01): 
    print("X_0 = %5.3f" % (X_0))
    for Y_0 in np.arange(-4, 4, 0.01):
        x = X_0
        y = Y_0
        k = 0
        delta = 999999.9
        for k in range(100): 
            old_x = x
            old_y = y
            x = -rho*old_x + llambda*np.sin(theta*old_y)
            y = -rho*old_y + llambda*np.sin(theta*old_x)
            delta = max(abs(x-old_x), abs(y-old_y))
        if delta>0.2: 
            basin_ID = -1   # non-convergence zone (oscillating) 
        else:
            basin_ID = int(100 + 10*x + y + 0.5)
        if basin_ID in basin_count:
            basin_count[basin_ID] += 1 
        else:
            basin_count[basin_ID] = 1
            n_basins = n_basins + 1
            if n_basins > n_cols - 1:
                # add color to color table for the new basin
                red   = np.random.rand()
                green = np.random.rand()
                blue  = np.random.rand()
                rgb = (red, green, blue)
                color.append(rgb)
                n_cols = n_cols + 1
            basin_color[basin_ID] = color[n_basins]
            basin_x[basin_ID] = x
            basin_y[basin_ID] = x
        list_x.append(X_0)
        list_y.append(Y_0)
        list_color.append(basin_color[basin_ID])

OUT.close()

for basin_ID,count in basin_count.items():
    col = str(basin_color[basin_ID])
    x   = basin_x[basin_ID]
    y   = basin_x[basin_ID]
    print("basinID: %4d count: %6d color: %8s x: %7.4f y: %7.4f" \
         % (basin_ID,count,col,x,y))

axes = plt.axes()
[axx.set_linewidth(0.2) for axx in axes.spines.values()]
axes.set_facecolor("white")   # background color
axes.margins(x=0)
axes.margins(y=0)
axes.tick_params(axis='both', which='major', labelsize=7)
axes.tick_params(axis='both', which='minor', labelsize=7)
plt.scatter(list_x, list_y, c=list_color, s=0.1)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.show()
