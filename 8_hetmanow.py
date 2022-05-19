from itertools import permutations

for permutation in permutations('000XXX0X0'):
    for i in range(3):
        for j in range(3):
            print(permutations[j+i*3], end='')
        print()
    print()

tab = [ [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0] ]

for i in range(8):
    for j in range(8):
        if tab[i][j] == 1:
            for k in range(j):
                if tab[i][k] == 1:
                    print('False')
            for x in range(i):
                if tab[x][j]:
                    print('False')

            pionowo = i + 1
            poziomo = j - 1
            
            while pionowo < 8 and poziomo >= 0:
                if tab[pionowo][poziomo] == 1:
                    print('False')
                pionowo += 1
                poziomo -= 1

            pionowo1 = i + 1
            poziomo1 = j + 1

            while 


        print(f'tab[{i}][{j}] = {tab[i][j]}')

    

print(tab)