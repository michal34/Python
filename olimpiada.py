class Person:
    def __init__(self, time, deadline, number):
        self.time = time
        self.deadline = deadline
        self.number = number

def compare(el1, el2):
    if el1.time < el2.time:
        return -1
    elif el1.time > el2.time:
        return 1
    else:
        if el1.deadline < el2.deadline:
            return -1
        elif el1.deadline > el2.deadline:
            return 1
        else:
            return 0

lista = []
liczbaFilmow = int(input())
for i in range(liczbaFilmow):
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    lista.append(Person(a, b, i))

for i in range(len(lista)):
    if lista[i].time > lista[i].deadline:
        del lista[i]
        

from functools import cmp_to_key
lista.sort(key=cmp_to_key(compare))
for i in lista:
    print(i.time, i.deadline, i.number)




# 5
# 4 5
# 2 4
# 5 3
# 1 9
# 3 10

