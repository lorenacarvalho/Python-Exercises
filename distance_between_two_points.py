from math import sqrt
import math
from unittest import result

def distance(x1, y1, x2, y2):
    result = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    extra = 'ola'
    return result, extra 

ponto_1 = input().split()
ponto_2 = input().split()
p1 = []
p2 = []

for i in ponto_1:
    p1.append(float(i))

for i in ponto_2:
    p2.append(float(i))

x1 = p1[0]
y1 = p1[1]
x2 = p2[0]
y2 = p2[1]

r_distance = distance(x1, y1, x2, y2)

a, b = r_distance
print(a)
print(b)
