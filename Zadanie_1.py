kwota = float(input())
nominaly = input().split(',')

reszta = []

while kwota != 0:
    kwota = round(kwota, 2)
    for i in reversed(nominaly):
        i = float(i)
        if i <= kwota:
            kwota -= i
            reszta.append(i)
            break
     
print((len(reszta), reszta))
