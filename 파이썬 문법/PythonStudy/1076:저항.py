# 색	값	곱
# black	0	1
# brown	1	10
# red	2	100
# orange3	1,000
# yellow4	10,000
# green	5	100,000
# blue	6	1,000,000
# violet7	10,000,000
# grey	8	100,000,000
# white	9	1,000,000,000

color = ('black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white')
D = dict(zip(color, range(10)))

a, b, c = input(), input(), input()
print((D[a]*10 + D[b]) * (10**D[c]))

# 최적화