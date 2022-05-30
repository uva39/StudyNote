import sys
fi = sys.stdin.readline

n, m = map(int, fi().split())
arr = list(map(int, fi().split()))

preSum = [0]*n
preSum[0] = arr[0]
for i in range(1, len(arr)):
    preSum[i] = preSum[i-1] + arr[i]
preSum.append(0)

for _ in range(m):
    start, end = map(int, fi().split())
    print(preSum[end-1] - preSum[start-2])