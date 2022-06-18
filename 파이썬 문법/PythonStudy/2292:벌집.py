n = int(input())

place, c = 1, 1
while place < n:
    place += 6*c
    c += 1
print(c)

n = int(input())

x = 1
while n > 3*x*x - 3*x + 1:
    x +=1
print(x)