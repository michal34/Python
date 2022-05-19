class Person:
    def __init__(self, family, animals):
        self.family = family
        self.animals = animals

osoba = [Person(1,3),
        Person(1,2),
        Person(3,1),
        Person(3,6),
        Person(1,3),
        Person(2,2)]
        

def compare(el1, el2):
    if el1.family < el2.family:
        return -1
    elif el1.family > el2.family:
        return 1
    else:
        if el1.animals > el2.animals:
            return -1
        elif el1.animals < el2.animals:
            return 1
        else:
            return 0

from functools import cmp_to_key
osoba.sort(key=cmp_to_key(compare))
for i in osoba:
    print(i.family, i.animals)