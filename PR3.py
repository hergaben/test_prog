import numpy as np
import random
import matplotlib.pyplot as plt

"""
rows = 4
cols = 4
a = np.random.randint(10, size=(rows,cols))
b = np.flipud(a)
ab = np.concatenate((a, b))

fig, ax = plt.subplots()
ax.imshow(a)
fig.set_figwidth(4)
fig.set_figheight(4)
plt.show()
"""
for i in range(3):
    for _ in range(3):
        k = random.randint(1, 3)
        m = random.randint(4, 7)
        g = random.randint(8, 10)
        u = random.randint(11, 13)
        sm = [[k, m, k, k, u, u, k, k, m, k],
              [m, m, k, k, g, g, k, k, m, m],
              [k, k, m, k, k, k, k, m, k, k],
              [k, k, k, m, g, g, m, k, k, k],
              [m, u, g, u, m, m, u, g, u, m]]
        b = np.flipud(sm)
        c = np.concatenate((sm, b))




    fig, ax = plt.subplots()
    ax.imshow(c)
    fig.set_figwidth(4)
    fig.set_figheight(4)


plt.show()