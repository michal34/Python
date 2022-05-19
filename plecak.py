waga_plecaka = int(input())

n = int(input())
tab = []

for i in range(n):
    przedmiot = input()
    a = przedmiot.split(' ')
    wartosc = int(a[1])/int(a[2])
    tab.append([wartosc,int(a[1]),int(a[2]),a[0]])
    
tab.sort()
plecak = []
print(f'\r\n{tab}\r\n')
    
for i in tab:
    if waga_plecaka - i[1] < 0:
        break
    else:
        waga_plecaka -= i[1]
        plecak.append([i[3],i[1],i[2]])
        
print(plecak)
print(waga_plecaka)