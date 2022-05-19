slowo = input('Wpisz slowo: ')

print('_ '*len(slowo))

zgadniete = []
litery = []
litery[:0] = slowo

for i in litery:
    zgadniete.append('_ ')
    
proby = 10
print('Masz 10 prob')

while proby > 0:
    litera = input('Wpisz litere: ')
    if litera in litery:
        for i in len(litery):
            if litery[i] == litera:
                zgadniete[i] = litera
                print('Zgadles litere')
    else:
        proby -= 1
        print('Zla odpowiedz')
        if proby == 0:
            print('Koniec gry')
        else:
            print(f'Zostaly ci {proby} zycia')
    if zgadniete == litery:
        print('Wygrales')
        break