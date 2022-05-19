def bubble_sort(tablica):

    for i in range(len(tablica)):
        for j in range(len(tablica) - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    print(tab)

tab = [12,4,5,6,1,2,987,432,15,5,91,2]
bubble_sort(tab)