# z is an 8-bit winning number if t >= T and (t - T) % 8 == 0

x = 1          # seed: 1st component, x0
y = 2          # seed: 2nd component, y0
T = 53         # must be >= 10
max = 200      # maximum for t, must be >= T
buffer = {}    # to store 9 previous values of x

for t in range(2, max): 

    if 4*x + 1 < 2*y:
        y = 4*y - 8*x - 2
        x = 2*x + 1
        d = 1        # t-th binary digit (unused)  
    else:
        x = 2*x
        y = 4*y
        d = 0        # t-th binary digit (unused)

    if t >= T - 8:
      buffer[t % 9] = x
      if t >= T:
          z = x - 256*buffer[(t-8) % 9] 

    if t >= T and (t - T) % 8 == 0:
        print(t, z, x) 
