# sine2D_orbit.py | find and plot basins of attraction of 2D sine map

import numpy as np
import matplotlib.pyplot as plt

def orbit(X_0, Y_0, llambda, theta, rho, n_iter):
    list_x = []
    list_y = []
    list_color = []
    x = X_0
    y = Y_0
    for iter in range(n_iter): 
        old_x = x
        old_y = y
        x = -rho*old_x + llambda*np.sin(theta*old_y)
        y = -rho*old_y + llambda*np.sin(theta*old_x)
        list_x.append(x)
        list_y.append(y)
        red   = 1.0*abs(np.sin(2.7 - 5.4*iter/n_iter)) 
        green = 0.8*abs(np.sin(0.8 + 8.0*iter/n_iter)) 
        blue  = 0.6*abs(np.sin(5.2 - 4.7*iter/n_iter))  
        alpha = 1.0
        rgb = (red, green, blue, alpha)
        list_color.append(rgb)
    return(list_x, list_y, list_color)

llambda  = [2.0, 0.04, 1.5, 10, 2.5, 2.0, 2.0] 
theta    = [1.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]           
rho      = [-0.5, -1, -1, -1, -1, -1, -0.5] 
mode     = ['s','p','p','p','p','p','s']  # 's' for scatter, 'p' for plot
n_iter   = [50000, 20000, 20000, 20000, 20000, 20000, 50000]
X_0 = [0.0, 1.0, 3.0, 2.0, 1.0, 3.0, 0.0]  
Y_0 = [3.0, 4.0, 4.0, 4.0, 4.0, 4.0, 3.0]   
n_plots = len(X_0)    

for plot in range(n_plots):
    (list_x, list_y, list_color) = orbit(X_0[plot], Y_0[plot], \
            llambda[plot], theta[plot], rho[plot], n_iter[plot])
    axes = plt.axes()
    [axx.set_linewidth(0.2) for axx in axes.spines.values()]
    axes.set_facecolor("black")   # background color
    axes.margins(x=0)
    axes.margins(y=0)
    axes.tick_params(axis='both', which='major', labelsize=7)
    axes.tick_params(axis='both', which='minor', labelsize=7)
    if mode[plot] == 's':
        plt.scatter(list_x, list_y, c=list_color, s=0.1)
    elif mode[plot] == 'p':
        for idx in range(n_iter[plot]-1):
            col = list_color[idx]
            xx = [list_x[idx], list_x[idx +1]]
            yy = [list_y[idx], list_y[idx +1]]
            plt.plot(xx, yy, linewidth = 0.4, c=col) 
    plt.show()
