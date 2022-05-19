n = int(input())
i = 0
f = 0
lista = []
def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

while i != n:
    f = f + 1
    if czy_pierwsza(f) == True:
        lista.append(f)
        i = i + 1

print(lista)