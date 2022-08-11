from sys import stdin
fi = stdin.readline

N, M = map(int, input().split())
Pokemons = [fi().rstrip() for _ in range(N)]

PD = dict()
for i, p in enumerate(Pokemons, 1):
    PD[p] = str(i)
    PD[str(i)] = p

for _ in range(M):
    a = fi().rstrip()
    print(PD[a])
