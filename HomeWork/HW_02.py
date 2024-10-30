import math
a = int(input())
b = int(input())
c = int(input())
D = b * b - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(round(x1, 1))
    print(round(x2, 1))
elif D == 0:
    x = -b / (2 * a)
    print(round(x, 1))
else:
    real_part = -b / (2 * a)
    imag_part = math.sqrt(abs(-D)) / abs(2 * a)
    print(f"{round(real_part, 1)}+{round(imag_part, 1)}i")
    print(f"{round(real_part, 1)}-{round(imag_part, 1)}i")