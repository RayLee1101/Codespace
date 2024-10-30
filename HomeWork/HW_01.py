import math
a = float(input(""))
b = float(input(""))
c = float(input(""))
x1 = (b * -1 + math.sqrt(b * b - 4 * a * c) )/ (2 * a)
x2 = (b * -1 - math.sqrt(b * b - 4 * a * c)) / (2 * a)
if x1 == x2:
    print("%.1f" % x1)
else:
    print("%.1f" % x1)
    print("%.1f" % x2)