def binary_search(lista, liczba):
    pierwszy_index = 0
    ostatni_index = len(lista) - 1

    while pierwszy_index <= ostatni_index:
        srodek = pierwszy_index + (ostatni_index - pierwszy_index) // 2

        if lista[srodek] == liczba:
            return srodek
        
        elif liczba < lista[srodek]:
            ostatni_index = srodek - 1

        else:
            pierwszy_index = srodek + 1

    return None


lista_a = [2,4,5,7,8,9,12,15]
liczba_a = 12
print(binary_search(lista_a, liczba_a))