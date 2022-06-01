import math
n = int(input())
klasy = []
slownik = {}

for i in range(n):
    slownik[f'{i}'] = []
    osoba = ''
    while osoba != '-':
        osoba = input()
        if osoba != '-':
            slownik[f'{i}'].append(osoba.split(' '))

for i in range(n):
    for j in range(len(slownik[f'{i}'])):
        for l in range(len(slownik[f'{i}'])):
            if float(slownik[f'{i}'][j][2]) > float(slownik[f'{i}'][l][2]):
                a = slownik[f'{i}'][j]
                slownik[f'{i}'][j] = slownik[f'{i}'][l]
                slownik[f'{i}'][l] = a
                
for i in range(n):
    d = len(slownik[f'{i}']) * 0.1
    d = math.ceil(d)
    for j in slownik[f'{i}'][:d]:
        print(j[0], j[1])
    print('-')