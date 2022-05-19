def binary_search(tab, left, right, x):
    srodek = (left + right) // 2
    
    if left <= right:
        if tab[srodek] == x:
            return srodek

        elif x < tab[srodek]:
            right = srodek - 1
            return binary_search(tab, left, right, x)

        else:
            left = srodek + 1
            return binary_search(tab, left, right, x)
    else:
        return -1

lista_a = [2,4,5,7,8,9,12,15]
x = 12
left = 0
right = len(lista_a) - 1

print(binary_search(lista_a, left, right, x))