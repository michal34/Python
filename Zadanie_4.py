def plecak(a, b, c, n):

    if n == 0 or a == 0:
        return 0
    
    if (b[n-1] > a):
        return plecak(a, b, c, n-1)
 
    else:
        return max(
            c[n-1] + plecak(
                a-b[n-1], b, c, n-1),
            plecak(a, b, c, n-1))
 
c = input().split(', ')
b = input().split(', ')
a = int(input())
n = len(c)

for i in range(len(c)):
    c[i] = int(c[i])
    
for i in range(len(b)):
    b[i] = int(b[i])

print(plecak(a, b, c, n))