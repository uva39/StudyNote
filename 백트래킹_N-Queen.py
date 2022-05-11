def promising(cdx):
    for i in range(cdx):
        if board[cdx] == board[i] or cdx - i == abs(board[cdx] - board[i]):
            return 0
    return 1

def n_queen(cdx):
    global count
    if cdx == n:
        count += 1
        return

    for i in range(n):
        board[cdx] = i
        if promising(cdx):
            n_queen(cdx + 1)

n = int(input())
count = 0
board = [0]*n

n_queen(0)
print(count)
