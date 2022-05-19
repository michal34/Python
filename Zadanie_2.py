n = int(input())
produkty = []

for i in range(n):
    produkt = input().split(' ')
    produkty.append(produkt)

a = int(input())
if a == 0:
    produkty.sort()
elif a == 1:
    for i in range(len(produkty)):
        for j in range(len(produkty)):
            if produkty[i][1] > produkty[j][1]:
                b = produkty[i]
                produkty[i] = produkty[j]
                produkty[j] = b
                
print(produkty)