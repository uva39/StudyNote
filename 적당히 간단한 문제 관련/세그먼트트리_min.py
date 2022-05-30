N = int(input())
Line = list(map(int, input().split()))
Point = list(map(int, input().split()))

MinP = [min(Point[:i]) for i in range(1, len(Point))]
# TODO: 세그먼트 트리 활용해서 최적화해야 함

result = 0
for x, y in zip(Line, MinP):
    result += x*y
print(result)
