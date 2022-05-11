import math
import sys
# 4 <= N <= 10000 범위의 N을 입력받고, N을 두 소수로 쪼개준다. 
# 이때, 두 소수의 차가 가장 가까운 방향으로 출력한다.


E = [True] * 10001
for i in range(2, int(math.sqrt(10002))+1):
    if E[i]:
        for j in range(i*2, 10001, i):
            E[j] = False
E = [i for i in range(len(E)) if E[i]]
E = E[2:]
# over is Initial Erastotenes List E.


times = int(input())
for _ in range(times):
    a = int(sys.stdin.readline())
    F = [x for x in E if x <= a]
    G = [x for x in F if x >= a//2]
    
    for x in G:
        if a - x in F:
            if x > a-x:
                print(a-x, x)
            else:
                print(x, a-x)
            break
