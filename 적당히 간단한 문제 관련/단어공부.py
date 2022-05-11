X = input()
Y = X.upper()
D = {i:0 for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

for y in Y:
    D[y] += 1

K = list(D.keys())
V = list(D.values())
M = max(V)

if V.count(M) > 1:
    print("?")
else:
    print(K[V.index(M)])
