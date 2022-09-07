import math
from math import fabs


def f(z):
    if (z < 76):
        l = z**4-29*math.atan(z)**2
    elif (76 <= z < 149):
        l = math.log(z**2,10)**7-(fabs(59-37*z**3))**6
    else:
        l = 1+61*z**4
    return l


print(f(32))