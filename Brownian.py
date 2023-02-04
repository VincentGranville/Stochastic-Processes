import numpy as np
import matplotlib.pyplot as plt

n = 10000
m = 5*n
T = []
X = []
T.append(0.0)
X.append(0.0)
np.random.seed(1979)
for k in range(1,m):
    u = np.random.uniform(0,1)
    if u < 0.5:
        X.append(X[k-1]-1)
    else:
        X.append(X[k-1]+1)
    T.append(T[k-1] + 1/n)

S = []
S.append(0.0)
for k in range(1,m):
    S.append(X[k]+S[k-1])

M = []
smooth = 2.5  # the larger, the smoother the moving average
M.append(0.0)
hn = int(smooth*np.sqrt(n))
for k in range(1,m):
    sum = 0.0
    for h in np.arange(-hn, hn+1):
        idx = k + h
        if idx >= m:  # fix for index outside the array range
            idx = m - 1 - (idx % n)
        elif idx < 0: # fix for index outside the array range
            idx = -idx
        sum += X[idx]
    sum /= (2*hn + 1)
    M.append(sum)

for k in range(1,m):
    X[k] = X[k]/(n**0.5)
    S[k] = S[k]/(n**1.5)
    M[k] = M[k]/(n**0.5)

axes = plt.axes()
axes.tick_params(axis='both', which='major', labelsize=8)
axes.tick_params(axis='both', which='minor', labelsize=8)
for axis in ['top','bottom','left','right']:
    axes.spines[axis].set_linewidth(0.5) 
plt.plot(T, X, linewidth = 0.4, color = 'green', alpha = 0.2)   # Brownian motion
plt.plot(T, S, linewidth = 0.8, color = 'orange', alpha = 0.8)  # integrated Brownian motion
plt.plot(T, M, linewidth = 0.8, color = 'red', alpha = 1.0)     # moving average process
plt.axhline(y = 0.0, color = 'grey', linestyle = '--', linewidth = 0.4)
plt.show()
