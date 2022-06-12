# 초기화
board = ['AAAAAAAA' for i in range(8)]

# 입력
for i in range(8):
    board[i] = input()

# 문제
c = 0
for i in range(8)[::2]:
    for j in range(8)[::2]:
        if board[i][j] == 'F':
            c += 1

for i in range(1, 8)[::2]:
    for j in range(1, 8)[::2]:
        if board[i][j] == 'F':
            c += 1

# 출력
print(c)