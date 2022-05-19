kwota = int(input())
nominaly = input().split(',')

reszta = []

for i in reversed(nominaly):
    i = float(i)
    if i <= kwota:
        kwota -= i
        reszta.append(i)
     
odpowiedz = (len(reszta), reszta)
print(odpowiedz)