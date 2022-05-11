import sys

n, SortType = map(int, input().split())

A = [(0,'')]*n
for i in range(n):
    A[i] = sys.stdin.readline().rstrip().split()
    A[i][0] = int(A[i][0])

if SortType == 1:
    A.sort(key = lambda x: x[0])
# lambda x: x[0] -> x가 (12, 98, 23)같은 시퀀스일때, [0]인 12를 기준으로 해서 정렬을 수행한다는 뜻이다.
else:
    A.sort(key = lambda x: (x[0], x[1]))
# lambda x: (x[0], x[1]) -> x[0]을 1순위, x[1]을 2순위로 고려해서 정렬한다. 인자가 늘어도 마찬가지의 뜻이다.

for a in A:
    print(' '.join(map(str, a)))

