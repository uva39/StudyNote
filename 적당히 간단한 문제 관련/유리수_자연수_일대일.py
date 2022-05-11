X = int(input())

n = 1
while X > (n*(n+1))//2:
    n += 1

b = X - ((n*(n-1))//2)
a = n - b + 1

if n % 2 == 1:
    print('{}/{}'.format(a,b))
else:
    print('{}/{}'.format(b,a))