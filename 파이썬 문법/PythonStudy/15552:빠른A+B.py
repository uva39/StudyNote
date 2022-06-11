from sys import stdin
fi = stdin.readline

t = int(fi())
for _ in range(t):
    a, b = map(int, fi().split())
    print(a+b)