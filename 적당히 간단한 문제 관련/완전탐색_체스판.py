# 흰색과 검은색이 공존하는 M*N크기의 보드에서
# 어떤 정사각형은 검은색, 나머지는 흰색으로 칠해져 있다.
# 이 보드를 잘라서 8*8 체스판을 만들려고 하는데
# 체스판은 체크무늬 형태로 칠해져있어야 한다.
# 보드에서 잘라냈을때, 바꿔서 칠해야 하는 색의 최소값을 구하라
# 체스판 색칠의 경우는 맨 왼쪽이 흰색인 경우, 검은색인 경우
# 두 가지 뿐이다.

# 생각
# 일단 전부 받아온다.
# N*M 판을 전체 경우의 수로 돌려야 한다.
# 그러기 위해서는 인덱스가 8을 넘지 않도록 조정을 해줘야 한다.
# 9*9에서 움직여서 조사할 수 있는 경우의 수는 2*2 4개이며,
# 10*10에서 움직여서 조사할 수 있는 경우의 수는 3*3 9개이고
# 11*11에서 움직여서 조사할 수 있는 경우의 수는 4*4 16개이다.
# 따라서, i는 N-7의 범위에서, j는 M-7의 범위에서 움직인다.
# 이후에 전체 경우의수를 다 돌면서
# W로 시작한 경우, B로 시작한 경우를 나누어서 판단한다.

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())

repair = []
for i in range(n - 7):
    for j in range(m - 7):
        firstW, firstB = 0, 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        firstW += 1
                    if board[k][l] != 'B':
                        firstB += 1
                else:
                    if board[k][l] != 'B':
                        firstW += 1
                    if board[k][l] != 'W':
                        firstB += 1
        # 메인의 board를 8x8 size로 자른 sliced board를, 두 경우(firstW, firstB)의 체스판에 대해서 대조.
        # 차를 전부 repair에 저장 후 최소를 구하면 됨.
        repair.append(firstW)
        repair.append(firstB)

print(min(repair))