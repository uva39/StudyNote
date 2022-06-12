T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())

    HOTEL = []
    for i in range(1, w+1):
        for j in range(1, h+1):
            HOTEL.append(f'{j}{i:0>2}')
    print(HOTEL[n - 1])