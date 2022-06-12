a = int(input())
b = int(input())
c = int(input())
result = str(a*b*c)

D = dict(zip(range(10), [0]*10))

for x in result:
    D[int(x)] += 1
for key in D:
    print(D[key])