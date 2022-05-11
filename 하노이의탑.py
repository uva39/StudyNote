def hanoi(N, start, via, end):
    if N == 1:
        print(start, '=>', end)
        return

    hanoi(N - 1, start, end, via)
    print(start, '=>', end)
    hanoi(N - 1, via, start, end)

hanoi(int(input()), 1, 2, 3)