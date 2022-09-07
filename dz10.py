import re


def item(table):
    n3 = []
    for i in table:
        for x in i:
            if x is None:
                i.remove(x)
    temp = []
    for x in table:
        if x not in temp:
            temp.append(x)
    table = temp
    for row in table:
        del row[2]
    for i in range(0, len(table)):
        stroka = table[i][1]
        stroka = stroka.split('%')
        stroka0 = stroka[0]
        stroka = stroka[1]
        stroka = stroka.split('@')
        gp = table[i][0]
        gp = gp.split(' ')
        if len(stroka0) == 1:
            stroka0 = '0' + stroka0
            table[i][1] = '0.' + stroka0 + '00'
        elif len(stroka0) == 3:
            table[i][1] = '1.0000'
        else:
            table[i][1] = '0.' + stroka0 + '00'
        n3.append([gp[1], table[i][1], stroka[1]])
    table = n3
    print(table)
    return table
        # print(table[i][0])
        # print(table[i][1])
        # print(stroka[1])




    # for i in table:
    #     i[2] = i[2].split('@')


# def transformer(i, value):
#     if i == 0:
#         replaced = value \
#             .replace(' ', '')
#         return replaced[3:]
#     if i == 1:
#         replaced = value
#         replaced = replaced[0:2]
#         value = replaced
#         digit_str = value.replace('%', '')
#         digit = float(digit_str) / 100
#         return f'{digit:.2f}'




    print(n3)

"""
table = ['М.Ц. Вомокиди',   '85%:vomokidi62@mail.ru',   'None',	   'М.Ц. Вомокиди'
         'Д.Р. Шатак',	    '22%:satak71@mail.ru',		'None',    'Д.Р. Шатак'
         'Р.Т. Нутян',	    '53%:nutan83@gmail.com',	'None',	   'Р.Т. Нутян'
         'Р.Т. Нутян',	    '53%:nutan83@gmail.com',	'None',	   'Р.Т. Нутян'
         'С.Ш. Ренилев',	'75%:renilev40@mail.ru',	'None',	   'С.Ш. Ренилев'
         'Р.Т. Нутян',	    '53%:nutan83@gmail.com',	'None',	   'Р.Т. Нутян']
"""

item(table=[['М.Ц. Вомокиди',	'85%:vomokidi62@mail.ru',	None,	   'М.Ц. Вомокиди'],
            ['Д.Р. Шатак',	    '22%:satak71@mail.ru',		None,    'Д.Р. Шатак'],
            ['Р.Т. Нутян',	    '53%:nutan83@gmail.com',	None,	   'Р.Т. Нутян'],
            ['Р.Т. Нутян',	    '53%:nutan83@gmail.com',	None,	   'Р.Т. Нутян'],
            ['С.Ш. Ренилев',	    '75%:renilev40@mail.ru',	None,	   'С.Ш. Ренилев'],
            ['Р.Т. Нутян',	    '53%:nutan83@gmail.com',	None,	   'Р.Т. Нутян']])