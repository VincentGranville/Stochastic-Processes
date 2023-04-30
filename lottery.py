x = 1 
y = 2
buffer = {}
buffer[0] = 0
buffer[1] = 1

for t in range(2,21): 

    if 4*x + 1 < 2*y:
        y = 4*y - 8*x - 2
        x = 2*x + 1
        d = 1        # binary digit 
    else:
        x = 2*x
        y = 4*y
        d = 0        # binary digit

    # buffer stores 9 previous vales of x
    buffer[t % 9] = x
    if t > 7:
        # winning numbers
        z = x - 256*buffer[(t-8) % 9] 
    else:
        z = float("NaN") # undefined number
    print(t, d, z, x, y)
