import glob
pliki = glob.glob("*.txt")

slownik = {}

for plik in pliki:
    with open(plik, 'r', encoding='utf-8') as f:
        zawartosc = f.readlines()
 
        for i in range(len(zawartosc)):
            zawartosc[i] = zawartosc[i].strip()
            
    nazwa_jezyka = plik.split('.')[0]
    slownik[nazwa_jezyka] = zawartosc

zdanie = input()
zdanie = zdanie.replace(",","")
slowa = zdanie.split(" ")

for i in range(len(slowa)):
    nowe_slowo = ""
    for litera in slowa[i]:
        if litera.isalpha():
            nowe_slowo += litera
    slowa[i] = nowe_slowo
    
punkty = {}

for lang in slownik:
    punkty[lang] = 0
    
for slowo in slowa:
    for lang in slownik:
        if slowo in slownik[lang]:
            punkty[lang] += 1
            
# detected_lang = None
# for lang in slownik:
#     if deceted_lang is None:
#         deceted_lang = lang
        
print(punkty)