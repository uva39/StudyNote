import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0]*(n+1)
tree = [0]*(n+1)


# 0이 아닌 마지막 비트의 의미란? https://www.youtube.com/watch?v=fg2iGP4e2mc
# 어떻게 구할까?
# (i & -i) : i와 -i를 비트 and연산하면 됨
# 연산 결과 예시: 0 1 2 3 4 5 6 7 8 -> 0 1 2 1 4 1 2 1 8
# 0이 아닌 마지막 비트: 내가 저장하고 있는 값들의 개수
# ex: 6, 7, 8 -> 2, 1, 8. 6은 5,6 / 7은 7 / 8은 1,2,3,4,5,6,7,8.


# 1부터 i번째 수까지의 누적합 계산
# i=7의 경우: a[7] 더하고 / i -= 1, a[6] 더하고 / i -= 2, a[4] 더하고 / i -= 4, 종료
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 0이 아닌 마지막 비트만큼 빼면서 이동(하위로, 앞쪽으로, 왼쪽으로 이동)
        i -= (i & -i)
    return result

# i번째 수를 업데이트 하는 함수
# i=7의 경우: a[7]에 x 저장하고 / i += 1, a[8]에 x 더하고 / i += 8, a[16]에 x 더하고 /
# i += 16, a[32]에 x 더하고 / ...(더하는 경우엔 0이 아닌 마지막 비트가 어느 순간부터 2의 n승 꼴이 됨) / 종료
def update(i, diff):
    # 전체 누적합인 tree[n] 아래의 부분합들에 대해서 반복
    while i <= n:
        tree[i] += diff
        # 0이 아닌 마지막 비트만큼 더하면서 이동(상위로, 뒷쪽으로, 오른쪽으로 이동)
        i += (i & -i)

# 구간 합 계산
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)


for i in range(1, n+1): # 배열의 원소들을 입력받음
    x = int(input())
    arr[i] = x
    update(i, x) # 바이너리 인덱스 트리를 업데이트

for i in range(m+k):
    a, b, c = map(int, input().split())
    # 업데이트의 경우
    if a == 1:
        # b번째 수를 c로 바꿈(Tree를 업데이트하는 관점에서는, c와 arr[b]의 차를 더함)
        update(b, c - arr[b])
        arr[b] = c

    # 구간 합 출력의 경우
    else:
        print(interval_sum(b, c))


'''
# 주석 제거 version

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0]*(n+1)
tree = [0]*(n+1)

def update(i, diff):
    while i <= n:
        tree[i] += diff
        i += (i & -i)

def interval_sum(start, end):
    def p_sum(i):
        result = 0
        while i > 0:
            result += tree[i]
            i -= (i & -i)
        return result
    return p_sum(end) - p_sum(start-1)

for i in range(1, n+1):
    x = int(input())
    arr[i] = x
    update(i, x)
    
for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c
    else:
        print(interval_sum(b, c))
    
'''