# chaos_solveFunctional.py | fixed-point iteration to compute invariant density f
# f_exact corresponds to alpha = llambda = 1: f(x) = (1/log(2)) * 1/(1+x)

import numpy as np
import matplotlib.pyplot as plt

M = 5000     # granularity
N = 500      # number of terms in the sum for functional equation 
llambda = 1  # must be <= 1
alpha   = 1
beta    = 1/alpha

OUT=open("solve.txt","w")

f_old = [] 
f_new = []
f_exact = []
x = []
for k in range(M+1):
    f_old.append(1.0)  # initialize f_0 to uniform[0,1]
    f_new.append(0.0)
    f_exact.append( (1/np.log(2)) / (1+k/M) )
    x.append(k/M)      # locations on X-axis
axes = plt.axes()
[axx.set_linewidth(0.2) for axx in axes.spines.values()]
axes.tick_params(axis='both', which='major', labelsize=7)
axes.tick_params(axis='both', which='minor', labelsize=7)

for iter in range(0,10):

    print("Fixed-point iteration:",iter)
    sum=0

    for k in range(M+1): 
        # loop over equally spaced arguments of f
        f_new[k]=0
        for n in range(1,N+1):  
            # loop over the terms in functional equation 
            y=(llambda/(x[k] + n))**beta  # x[k] = k/M
            y=int(0.5 + M*y)              # must have: 0 <= y <= M
            if y <= M+1: 
                f_new[k] += f_old[y]*beta*(llambda**beta)/((x[k]+n)**(1+beta))
            else:
                print("Out of range error (ignored):",iter,k,y)
        sum += f_new[k]

    for k in range(0,M+1):
        f_new[k] = M*f_new[k]/sum  # must integrate to 1 (it's a density)
        f_old[k] = f_new[k] 
    
    for k in range(M+1): 
        OUT.write("%6d\t%6d\t%6.4f\t%6.4f\n" % (iter,k,x[k],f_new[k]))
    plt.plot(x,f_new,linewidth=0.3) 

OUT.close()

plt.plot(x,f_new,linewidth=0.3)
plt.plot(x,f_exact,color='red',linewidth=0.6)
plt.show()



