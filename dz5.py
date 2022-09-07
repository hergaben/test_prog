def main(y):
    r1 = 0
    n = len(y)
    y.insert(0, 0)
    for i in range(1, len(y)):
        r1 += 28*(57*(y[n+1-i])**3)**6
    return 13*r1