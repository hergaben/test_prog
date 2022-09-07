def main(x):
    ver = x[2]
    while True:
        if ver == 'SHEN':
            ver = x[0]
            continue
        elif ver == 'P4':
            ver = 10
            continue
        elif ver == 'C++':
            ver = x[4]
            continue
        elif ver == 'MQL5':
            ver = x[4]
            continue
        elif ver == 'BLADE':
            ver = 9
            continue
        elif ver == 'STAN':
            ver = x[1]
            continue
        elif ver == 'STON':
            ver = x[1]
            continue
        elif ver == 'D':
            ver = 4
            continue
        elif ver == 'STAN':
            ver = 5
            continue
        elif ver == 'STON':
            ver = x[1]
            continue
        elif ver == 'D':
            ver = 8
            continue
        elif ver == 1969:
            ver = 0
            continue
        elif ver == 2010:
            ver = 1
            continue
        elif ver == 1969:
            ver = 2
            continue
        elif ver == 2010:
            ver = 3
            continue
        elif ver == 1969:
            ver = 6
            continue
        elif ver == 2010:
            ver = 7
            continue
        else:
            return ver

print(main(['C++', 2010, 'SHEN', 1969, 'STAN']))




def main(x):
    h0 = {x[2]: 'SHEN', x[0]: 'C++', x[4]: 'STAN', x[1]: 1969}
    h1 = {x[2]: 'SHEN', x[0]: 'C++', x[4]: 'STAN', x[1]: 2010}
    h2 = {x[2]: 'SHEN', x[0]: 'C++', x[4]: 'STON', x[1]: 1969}
    h3 = {x[2]: 'SHEN', x[0]: 'C++', x[4]: 'STON', x[1]: 2010}
    h4 = {x[2]: 'SHEN', x[0]: 'C++', x[4]: 'D'}
    h5 = {x[2]: 'SHEN', x[0]: 'MQL5', x[4]: 'STAN'}
    h6 = {x[2]: 'SHEN', x[0]: 'MQL5', x[4]: 'STON', x[1]: 1969}
    h7 = {x[2]: 'SHEN', x[0]: 'MQL5', x[4]: 'STON', x[1]: 2010}
    h8 = {x[2]: 'SHEN', x[0]: 'MQL5', x[4]: 'D'}
    h9 = {x[2]: 'SHEN', x[0]: 'BLADE'}
    h10 = {x[2]: 'P4'}

    for value in h9.values():
        for key in h9.keys():
            for i in x:
                if key == i == value:
                    return True
                else:
                    return False
"""
    for i in x:
        for value in h9.values():
            if i == value:
                return True
            else:
                return False
"""

print(main(['BLADE', 2010, 'SHEN', 1969, 'STAN']))



def main(x):
    if x[2] == 'P4':
        return 10
    if x[2] == 'SHEN':
        if x[0] == 'BLADE':
            return 9
        if x[0] == 'MQL5':
            if x[4] == 'D':
                return 8
            if x[4] == 'STON':
                if x[1] == 2010:
                    return 7
                if x[1] == 1969:
                    return 6
            if x[4] == 'STAN':
                return 5
        if x[0] == 'C++':
            if x[4] == 'D':
                return 4
            if x[4] == 'STON':
                if x[1] == 2010:
                    return 3
                if x[1] == 1969:
                    return 2
            if x[4] == 'STAN':
                if x[1] == 2010:
                    return 1
                if x[1] == 1969:
                    return 0


print(main(['C++', 2010, 'SHEN', 1969, 'STAN']))