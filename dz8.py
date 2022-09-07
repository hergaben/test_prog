def main(x):
    x = x.replace(';', '')
    x = x.replace('}', '} ')
    x = x.replace('{', ' {')
    a = []
    x = x.split('`')
    a.extend(x)
    for i in range(len(x)):
        if a[i] == '@' and a[i + 1] != ' ':
            a.insert(i + 1, ' ')
    x = ''.join(a)
    b = {}
    k = x.split('"')
    x = ' '.join(k)
    k = x.split()
    for j in range(len(k)):
        for r in range(len(k)):
            for p in range(len(k)):
                if k[p] == '@' and k[r] == '{' and k[j] == '}':
                    b[k[p + 1]] = k[r+1:j]
                    print(b)
    print(b)
    return b


#main('do \begin @"azausso" = { `ismais ; `larira ;`qusore }.\end. \begin @"lalaus_922" = { `biaedso_439 ; `usquge }. \end. od')
main('do \begin @"lalean"={ `esso_108 ;`orus_713 ; `usreso; `cege_122 }.\end. \begin @"iseror" ={ `dixe ; `rasola_192 ; `xevete }. \end. \begin @"qulege" ={ `azaedxe_401; `rezaen_176 ;`onlete_897 ; `tiuste_440 }.\end. od')


#True
def main(x):
    x = x.replace(';', ' ')
    x = x.replace('}', ' } ')
    x = x.replace('{', ' { ')
    a = []
    x = x.split('`')
    a.extend(x)
    for i in range(len(x)):
        if a[i] == '@' and a[i + 1] != ' ':
            a.insert(i + 1, ' ')
    x = ''.join(a)
    b = {}
    k = x.split('"')
    x = ' '.join(k)
    k = x.split()
    r1 = []
    r2 = []
    for j in range(len(k)):
        if k[j] == '{':
            j += 1
            r1.append(j)
    for r in range(len(k)):
        if k[r] == '}':
            r2.append(r)
    m = 0
    for p in range(len(k)):
        if k[p] == '@':
            b[k[p + 1]] = k[r1[m]:r2[m]]
            m += 1
    return b


#Chek
def main(x):
    x = x.replace(';', ' ')
    x = x.replace('}', ' } ')
    x = x.replace('{', ' { ')
    a = []
    x = x.split('`')
    a.extend(x)
    for i in range(len(x)):
        if a[i] == '@' and a[i + 1] != ' ':
            a.insert(i + 1, ' ')
    x = ''.join(a)
    b = {}
    k = x.split('"')
    x = ' '.join(k)
    k = x.split()
    r1 = []
    r2 = []
    print(k)
    for j in range(len(k)):
        if k[j] == '{':
            j += 1
            r1.append(j)
    print(r1)
    for r in range(len(k)):
        if k[r] == '}':
            r2.append(r)
    print(r2)
    m = 0
    for p in range(len(k)):
        if k[p] == '@':
            b[k[p + 1]] = k[r1[m]:r2[m]]
            #b[k[p + 1]] = k[36:39]
            m += 1
    return b


#print(main('do \begin @"azausso" = { `ismais ; `larira ;`qusore }.\end. \begin @"lalaus_922" = { `biaedso_439 ; `usquge }. \end. od'))
#print(main('do \begin @"lalean"={ `esso_108 ;`orus_713 ; `usreso; `cege_122 }.\end. \begin @"iseror" ={ `dixe ; `rasola_192 ; `xevete }. \end. \begin @"qulege" ={ `azaedxe_401; `rezaen_176 ;`onlete_897 ; `tiuste_440 }.\end. od'))
#print(main('do \\begin @"onbiza" ={ `xere ; `xeor_443; `orbi_425; `bece_674\n}.\\end. \\begin @"rea" = { `rira ;`ausor}. \\end.\\begin @"zaso" = {\n`riqu_572 ; `racere ; `xexeri_293 ; `dima }. \\end.\\begin @"tedi_641" =\n{ `leordi_118; `mainle ; `onqu_960 }. \\end. od'))
#print(main('do \\begin @"vema"= { `dibi_146 ; `usar ; `leater }. \\end.\\begin\n@"esedre" = { `maisre_699; `ribiri ; `anri; `iszaso }. \\end.\\begin\n@"laer_937" = {`vedi ; `isis_496 ; `zaenan; `titeis}. \\end. od'))
#print(main('do\\begin @"eddite" = { `atra; `esbe ;`isor_3}. \\end. \\begin @"orat"\n={`erinza;`reedza; `anedus_224 }.\\end. od'))