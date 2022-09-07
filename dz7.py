

def main(x):
    y = bin(x)
    y = list(y)
    while len(y) < 34:
        y.insert(2, '0')
    y.reverse()
    g = []
    g.extend(y[18:30])
    g.extend(y[0:5])
    g.extend(y[5:18])
    g.extend(y[30:32])
    g.reverse()
    v = ''.join(g)
    q = int(v, base=2)
    return q

print(main(0xd277d547))