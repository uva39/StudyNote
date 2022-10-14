import sys
input = sys.stdin.readline

def d(month, day):
    ans = day
    for i in range(1, month):
        if i == 2:
            ans += 28
        elif i in (4, 6, 9, 11):
            ans += 30
        else:
            ans += 31
    return ans

n = int(input())
temp = [list(map(int, input().split())) for _ in range(n)]
a = [(d(m1, d1), d(m2, d2)) for m1, d1, m2, d2 in temp] # x: 꽃이 피는 날 / y: 지는 날
a.sort(key=lambda x:(x[0], -x[1]))
left, right = d(3, 1), d(11, 30)
print(a)
print(left, right)

cnt = 0
while :
    for:
        if:
    if:
