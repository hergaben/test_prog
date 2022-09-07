import math


def main(b, z, n, a):
    g = 0
    s = 1
    f = 1
    c = 1
    j = 1
    k = 1


    for c in range(c, b+1):
        g += + 40 * z ** 2 + 61 * math.log2(z) ** 3 + 31 * (c ** 4)
        print(g)

    for j in range(1, a+1):
        for k in range(1, n+1):
            f *= (j ** 2 + 1 + k ** 3) ** 4 - 88 * (math.floor(z)) ** 5 - 1
            print('f',f)


    return g+f

print(main(5, 0.82, 2, 3))



import math


def main(b, z, n, a):
    r1 = 0
    r2 = 1
    for c in range(1, b+1):
        r1 += 40*(z**2)+61*(math.log2(z))**3+31*(c**4)
    for i in range(1, a+1):
        for k in range(1, n+1):
            r2 *= (i**2+1+k**3)**4-88*(math.floor(z))**5-1
    return r1 + r2


print(main(7, 0.6, 6, 5))