def fill_star(size, x, y):
    if size == 1: # 종료조건
        arr[y][x] = '*'
        return

    nextSize = size // 3
    # 3배씩 감소
    for dy in range(3):
        for dx in range(3):
            if dy != 1 or dx != 1:
                fill_star(nextSize, x + dx * nextSize, y + dy * nextSize)
                # 오른쪽, 아래로만 가는 방향벡터 느낌으로 1개당 8번 재귀를 실행함


n = int(input())

arr = [[' ' for _ in range(n)] for _0 in range(n)] # 이차원 리스트 초기화
fill_star(n, 0, 0) # 재귀적으로 구하기
for a in arr:
    print(*a, sep='')