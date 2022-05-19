import copy

slownik = {}

a = int(input())

for i in range(a):
    miasto = input().split(' ')
    if miasto[0] not in slownik:
        slownik[miasto[0]] = [miasto[1]]
    else:
        slownik[miasto[0]].append(miasto[1])
    if miasto[1] not in slownik:
        slownik[miasto[1]] = [miasto[0]]
    else:
        slownik[miasto[1]].append(miasto[0])
    
print(slownik)

visited_city = {}

for i in slownik.keys():
    visited_city[i] = False
    
first_city = input('Poczatkowe miasto: ')
last_city = input('Koncowe miasto: ')

current_city = [first_city]
next_city = []
distance = 0

while first_city != last_city:

    first_city = current_city.pop(0)
    visited_city[first_city] = True
    
    
    for connected_city in slownik[first_city]:
        if not visited_city[connected_city]:
            next_city.append(connected_city)

    if not current_city:
        current_city = copy.deepcopy(next_city)
        next_city = []
        distance += 1
        
tab1 = []
for i in visited_city:
    tab1.append(i)
    
print(tab1[0])
for i in tab1:
    print('-->')
    print(i)
    
print('\r\n', visited_city)
print(distance)
    
    