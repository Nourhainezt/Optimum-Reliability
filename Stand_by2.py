from __future__ import division
import math
from math import exp, factorial

t = int(input("Give mission duration(h): "))
lamb=float(input("Give lambda: "))
R =float(input("Give the optimal Reliability: "))

y=1
s=0
n=0
X=lamb*t
RR=0
# def suma(s,y):
#     for k in range(y):
#
#         print("k",k)
#         print(X**k)
#         s += (X**k/math.factorial(k))
#         print("s", s)
while s*float(exp(-(lamb*t)))<R:
    #print("lamb",exp(-(lamb*t)))
    for k in range(y):
        # print("k", k)
        # print(X ** k)
        s += (X ** k / math.factorial(k))
       # print("s", s)
    y += 1
    n +=1
print('Number of identical components in passive redundancy')
print(n)
