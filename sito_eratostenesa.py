def sito(n):
    tab = [True]*(n+1)
    tab[0] = tab[1] = False
    for i in range(2, int(n**(0.5))+1):
        if tab[i]:
           for y in range(i, n+1, i):
                if y != i:
                    tab[y] = False
    for z in range(0, len(tab)):
        if tab[z] == True:
            print(z)

print(sito(100000000))