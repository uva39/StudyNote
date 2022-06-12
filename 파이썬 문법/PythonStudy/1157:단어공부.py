# 입력
word = input().upper()

# 문제풀이
D = dict()
for x in word:
    if x in D:
        D[x] += 1
    else:
        D[x] = 1

M = max(D.values())
K = []
for key, value in D.items():
    if value == M:
        K.append(key)

if len(K) == 1:
    print(K[0])
else:
    print('?')