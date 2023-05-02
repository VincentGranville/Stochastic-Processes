# w is an 8-bit winning number if t >= T and (t - T) % 8 == 0

t = 0
y = 2   # 1        # seed: 1st component, y0 (for t = 0)
z = 5   # 2        # seed: 2nd component, z0 (for t = 0)
T = 43         # must be >= 10
max = 200      # maximum for t, must be >= T
buffer = {}    # to store 9 previous vales of x
x0 = 0         # irrational number represented by the digits 

for t in range(1, max): 

    if z < 2*y:
        y = 4*y - 2*z
        z = 2*z + 3
        d = 1        # t-th binary digit (unused)  
    else:
        y = 4*y
        z = 2*z - 1
        d = 0        # t-th binary digit (unused)
  
    x0 += d * 1/2**t 

    if t >= T - 8:
      buffer[t % 9] = z
      if t >= T:
          w = (z - 256*buffer[(t-8) % 9] + 255) >> 2  

    if t >= T and (t - T) % 8 == 0:
        print(t, w, d, z) 

print("\nNumber x0:", x0)
