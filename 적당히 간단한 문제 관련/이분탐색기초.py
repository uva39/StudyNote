N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) 

while start <= end:
    mid = (start+end) // 2
    log = sum(x - mid for x in tree if x >= mid)
    
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)