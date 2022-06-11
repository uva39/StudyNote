from sys import stdin
fi = stdin.readline

t = int(fi())
for _ in range(t):
    word = fi().rstrip()
    result = 0
    counter = 1
    for x in word:
        if x == 'X':
            counter = 1
            continue
        else:
            result += counter
            counter += 1
    print(result)