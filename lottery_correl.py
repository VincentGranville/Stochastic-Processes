# Compute binary digits of X, p*X, q*X backwards (assuming X is random)
# Only digits after the decimal point (on the right) are computed
# Compute correlations between digits of p*X and q*X
# Include carry-over when performing grammar school multiplication

import numpy as np

# main parameters
seed = 105
np.random.seed(seed)
kmax = 1000000
p  = 5
q  = 3

# local variables
X, pX, qX = 0, 0, 0
d1, d2, e1, e2 = 0, 0, 0, 0
prod, count = 0, 0 

# loop over digits in reverse order
for k in range(kmax): 

    b = np.random.randint(0, 2)  # digit of X
    X = b + X/2  

    c1 = p*b
    old_d1 = d1
    old_e1 = e1 
    d1 = (c1 + old_e1//2) %2  # digit of pX
    e1 = (old_e1//2) + c1 - d1
    pX = d1 + pX/2

    c2 = q*b
    old_d2 = d2
    old_e2 = e2 
    d2 = (c2 + old_e2//2) %2  #digit of qX
    e2 = (old_e2//2) + c2 - d2
    qX = d2 + qX/2

    prod  += d1*d2
    count += 1 
    correl = 4*prod/count - 1

    if k% 10000 == 0:  
        print("k = %7d, correl = %7.4f" % (k, correl))  

print("\np = %3d, q = %3d" %(p, q))
print("X = %12.9f, pX  = %12.9f, qX  = %12.9f" % (X, pX, qX))
print("X = %12.9f, p*X = %12.9f, q*X = %12.9f" % (X, p*X, q*X))    
print("Correl = %7.4f, 1/(p*q) = %7.4f" % (correl, 1/(p*q))) 
