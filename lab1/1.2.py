from numpy import arange

for x in arange(-1.5, 1.5, 0.15):
    y = x**8-0.4*x**3-1.24
    if y < 0:
        print(f"{x:.2f}, {y:.2f}")