def insert_sort(tablica):

    for i in range(1, len(tablica)):
        a = tablica[i]
        x = i -1

        while x >= 0 and a < tablica[x]:
                tablica[x + 1] = tablica[x]
                x -= 1
        tablica[x + 1] = a
    print(tablica)

tab = [2,5,7,21,2,9,1]
insert_sort(tab)