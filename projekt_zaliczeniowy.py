data = {}
pracownicy = []

n = int(input())
tab = []

for i in range(n):
    a = input()
    tab.append(a)
    
for i in (tab):
    
    if i[0] == 'a' and i[2] == 'w' and i[1] == ' ':
        a = i.split(' ')
        data[a[2]] = [[],[int(a[3])]]
        
    elif i[0] == 'a' and i[2] == 'e' and i[1] == ' ':
        a = i.split(' ')
        pracownicy.append(a[2])
        data[a[3]][0].append(a[2])
        
    elif i[0] == 'd' and i[2] == 'w' and i[1] == ' ':
        a = i.split(' ')
        del data[a[2]]
        
    elif i[0] == 'm' and i[1] == ' ':
        a = i.split(' ')
        idpracownika = a[1]
        nazwa_oddzialu = a[2]
        nazwa_pracownika = pracownicy[int(idpracownika)]
        lista = []
        for b in data:
            if nazwa_pracownika in data[b][0]:
                for a in range(len(data[b][0])):
                    if data[b][0][a] != nazwa_pracownika:
                        lista.append(data[b][0][a])
                data[b][0] = lista
        data[nazwa_oddzialu][0].append(nazwa_pracownika)
        
    elif i[0] == 'e' and i[2] == 'w' and i[1] == ' ':
        a = i.split(' ')
        b = data[a[2]]
        b[1][0] = int(a[4])
        data[a[3]] = b
        del data[a[2]]
    
    elif i[0] == 'e' and i[2] == 'e' and i[1] == ' ':
        a = i.split(' ')
        przed_zmiana = pracownicy[int(a[2])]
        pracownicy[int(a[2])] = a[3]
        for g in data:
            if len(data[g][0]) == 1:
                data[g][0][0] = a[3]
            else:
                for b in range(len(data[g][0]) - 1):
                    if data[g][0][b] == przed_zmiana:
                        data[g][0][b] = a[3]
        
    elif i[0] == 's' and i[1] == ' ':
        ilosc_zmian = i.split(' ')[1]

        for c in data:
            tab2 = []
            tab3 = []
            
            if int(ilosc_zmian) == 0:
                if len(data[c][0]) < data[c][1][0]:
                    tak = ','.join(data[c][0])
                    print(f'\n(niedobór pracowników){c}:{tak}.')
                else:
                    cos = []
                    for i in range(data[c][1][0]):
                        cos.append(data[c][0][i])
                        
                    tak = ','.join(cos)
                    print(f'\n{c}:{tak}.')
            else:
                wielkosc_zmiany = data[c][1][0]
                ilosc_pracownikow = len(data[c][0])
                faktyczna_liczba_zmian = 0
                if int(ilosc_pracownikow) == 0:
                    faktyczna_liczba_zmian = 0
                else:
                    faktyczna_liczba_zmian = (int(ilosc_zmian) * int(wielkosc_zmiany)) % int(ilosc_pracownikow)
                
                for d in range(ilosc_pracownikow):
                    if d > faktyczna_liczba_zmian - 1:
                        tab3.append(data[c][0][d])
                    else:
                        tab2.append(data[c][0][d])
                        
                for e in tab2:
                    tab3.append(e)
                    
                data[c][0] = tab3
                
                if len(data[c][0]) < data[c][1][0]:
                    tak = ','.join(data[c][0])
                    print(f'\n(niedobór pracowników){c}:{tak}.')
                else:
                    
                    cos = []
                    for i in range(data[c][1][0]):
                        cos.append(data[c][0][i])
                        
                    tak = ','.join(cos)
                    print(f'\n{c}:{tak}.')
            
    else:
        print('Zła komenda')