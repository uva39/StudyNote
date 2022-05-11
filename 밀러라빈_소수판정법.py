import math
import sys

# 페르마 소정리의 역은 어떤 경우에서 성립하는가?에 관한 정리 : 밀러 - 라빈 테스트
# 이를 활용하면 특별한 a값들에 대해서 밀러 - 라빈 테스트를 했을 때
# 소수를 훨씬 더 빠르게 판정할 수 있다.
# long long integar 범위에서는 A = [2,7,61]이다. 
# 페르마 소정리 : 소수 n과 n의 배수가 아닌 a는 다음을 만족.

# a^(n-1) = 1 (mod n)
def miller_rabin(n, a):
    d = (n - 1) // 2
    while (d % 2 == 0):
        if (pow(a, d, n) == n-1): 
            return True
        d //= 2
    # for 0 <= r <= s-1, a^((2^r)d) = -1 (mod n) 이면 "아마도 소수일 것 같다." - 2번조건
    tmp = pow(a, d, n)
    return True if tmp == n-1 or tmp == 1 else False
    # a^d = +- 1 (mod n) - 1번조건


def isPrime(n):
    if n <= 1:
        return False
    if n <= 100:
        if check[n]:
            return True
        else:
            return False
            # 100 이하의 수에 대해서는 밀러-라빈 테스트를 쓰기보다는 에라스토테네스의 체로 걸러줌

    for a in A:
        if not miller_rabin(n, a):
            return False
    return True
    # n이 밀러-라빈 특이값 배열 A 안의 모든 a에 대해서 밀러-라빈 테스트를 만족한다면
    # n은 소수이다. (만약, 현재의 A로는 감당 불가능한 엄청나게 큰 값이 주어지면, A를 확장해야 한다.)
    # 지금은 A가 10^15 보다 조금 더 넓은 수준의 범위를 커버 가능하기에 소수라고 단정짓기 가능.

# 에라스토테네스의 체
check = [True] * 101
for i in range(2, int(math.sqrt(102))+1):
    if check[i]:
        for j in range(i*2, 101, i):
            check[j] = False

t = int(input())
A = [2, 7, 61]
cnt = 0

for _ in range(t):
    a = int(sys.stdin.readline()) * 2 + 1
    if isPrime(a):
        cnt += 1
print(cnt)