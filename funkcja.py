f = input('wzór funkcji = ')
x0 = float(input('x0: '))
x1 = float(input('x1: '))
n = int(input('n: '))

h = float((x1 - x0)/n)
x = x0

wynik = []

for i in range(n) :

    y = eval(f)
    x += h
    y2 = eval(f)
    pole = ((y+y2)/2)*h
    print(y, y2)
    wynik.append(pole)

print(sum(wynik))