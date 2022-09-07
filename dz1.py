import math


def main(y):
    k = (40*y**3)**6-(60*(1+y**3+86*y**2))
    o = 69*(math.cos(6*y**2))-53*y**4
    m = (y/91-30*y**3)**5
    return k/o-m


