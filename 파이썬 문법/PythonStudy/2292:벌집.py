n = int(input())

place, c = 1, 1
while place < n:
    place += 6*c
    c += 1
print(c)