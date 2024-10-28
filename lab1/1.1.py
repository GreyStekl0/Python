import math as m

x, a = int(input()), int(input())

if x < 1:
    y = a * m.log(x) + abs(x) ** (1/3)
elif 1 < x < 10:
    y = 2 * a * m.cos(x) + 3 * x ** 2
else:
    y = 5 * 10 ** -7 + m.tan(x)

print(y)