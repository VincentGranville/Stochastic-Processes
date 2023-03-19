import numpy as np

b = np.sqrt(2)/2   
a = 1-b
z = np.log(2)  

prod = 1.0
beta = b/(1-a)
alpha = a/(1-b)

if z > beta: 
  sum   = b
  digit = 1
else:
  sum   = a
  digit = 0

prod = sum
print("digit %3d = %1d" % (0, digit))

for k in range(1, 60):
    beta  = sum + prod * b/(1-a)  
    alpha = sum + prod * a/(1-b)
    if alpha < z:
         prod  = prod * b
         digit = 1
    else: 
        prod  = prod * a
        digit = 0
    sum += prod 
    print("digit %3d = %1d" % (k, digit))
print ("sum = %14.13f, z = %14.13f" % (sum, z))
