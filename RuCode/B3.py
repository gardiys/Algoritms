import math
x1,y1,x2,y2 = [int(i) for i in input().split()]

a = (x1**2 + y1**2) ** 0.5
b = (x2**2 + y2**2) ** 0.5

cos_a = (x1*x2 + y1*y2) / (a*b)
print(math.acos(cos_a))