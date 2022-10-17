import sys
input = sys.stdin.readline

def f():
    now = 301
    ans = 0
    while now < 1201:
        next = now
        for x in arr:
            if next <= x[1] and x[0] <= now:
                next = x[1]
        if next == now:
            print(0)
            return
        ans += 1
        now = next
    print(ans)

n = int(input())
arr = [[0, 0] for _ in range(n)]
for i in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    arr[i] = m1*100 + d1, m2*100 + d2
f()