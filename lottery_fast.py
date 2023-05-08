import gmpy2

def big_seed(offset, beta):

    beta_1  = beta * (2**(2*offset)) 
    alpha_1 = int(gmpy2.isqrt(beta_1)) 
    y0_1 = 2 * (beta_1 - alpha_1*alpha_1)
    z0_1 = 1 + 4*alpha_1
    return(y0_1, z0_1)


n = 40       # number of digits to compute 
offset = 10  # digits start at location 1 + offset
y, z = big_seed(offset, 2)
digits = {}

for t in range(1, n): 
    if z < 2*y:
        y = 4*y - 2*z
        z = 2*z + 3
        digits[t + offset] = 1        
    else:
        y = 4*y
        z = 2*z - 1
        digits[t + offset] = 0   
    if t > 8 and t % 8 == 5:
        w = 0
        for k in range(8):
            w += digits[t + offset - k] * (2**k)
        print(t + offset, w)

print("seed:", y, z)
