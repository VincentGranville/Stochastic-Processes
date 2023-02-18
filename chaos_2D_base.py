# chaos_2D_base.py | compute Kolmogorov-Smirnov Delta distance in test of independence

import numpy as np
import matplotlib.pyplot as plt

def simulation(b0,b1,n,m):

    Delta    = 0.0; # Kolmogorov-Smirnov distance
    arr_pi   = [0] * n
    arr_pi_0 = [0] * n
    
    for iter in range(0, n): 
        alpha1 = np.random.uniform(0.0, 1.0)
        alpha2 = np.random.uniform(0.0, 1.0)
        alpha3 = np.random.uniform(0.0, 1.0)
        count = 0
        for k in range (2, m): 
            x[k] = (b1 * x[k-1] + b0* x[k-2]) % 1
            if x[k-2]<alpha1 and x[k-1]<alpha2 and x[k]<alpha3:
                count += 1
        pi   = (count/(m-1))**(1/3)
        pi_0 = (alpha1 * alpha2 * alpha3)**(1/3)
        arr_pi.append(pi)
        arr_pi_0.append(pi_0)
        diff = abs(pi - pi_0)
        if diff > Delta:
            Delta = diff
        OUT.write("%3d\t%3d\t%.4f\t%.4f\t%.4f\t%6.5f\t%6.5f\n" \
             % (b0,b1,alpha1,alpha2,alpha3,pi,pi_0))

    return(Delta, arr_pi, arr_pi_0) 


n = 100
m = 100000
seed = 543
np.random.seed(seed)
x = [0] * m   # initialize array of size m
x[0] = 0.5       # seed: X_0
x[1] = np.log(2) # seed: X_1

OUT=open("base2d.txt","w")
OUT.write("b0\tb1\talpha0\talpha1\talpha2\tpi\tpi_0\n")
axes = plt.axes()
[axx.set_linewidth(0.2) for axx in axes.spines.values()]
axes.tick_params(axis='both', which='major', labelsize=7)
axes.tick_params(axis='both', which='minor', labelsize=7)
axes.set_xlim(0.0, 1.0)
axes.set_ylim(0.0, 1.0)
plt.plot([0,1], [0,1], 'k-', linewidth=0.2)

b0 = -5; b1 =4
(Delta, arr_pi, arr_pi_0) = simulation(b0, b1, n, m)
print("base = (%2d, %3d) | Kolmogorov-Smirnov distance: %6.4f" % (b0, b1, Delta))
plt.scatter(arr_pi, arr_pi_0,s=1.0)

b0 = 3; b1 =-2
(Delta, arr_pi, arr_pi_0) = simulation(b0, b1, n, m)
print("base = (%2d, %3d) | Kolmogorov-Smirnov distance: %6.4f" % (b0, b1, Delta))
plt.scatter(arr_pi, arr_pi_0,s=1.0)

plt.show()
OUT.close()
