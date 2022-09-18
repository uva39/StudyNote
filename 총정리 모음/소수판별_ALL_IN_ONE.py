import math
import sys



def isPrime_sqrt(n:int) -> bool:
    """
    소수인지 확인할 수 n을 입력받으면, sqrt(n)+1까지 쭉 나눠보고 답을 반환하는 함수입니다.
    시간복잡도는 O(sqrt(N))이고, 이정도만 해도 충분히 쓸만합니다.
    """
    t = int(n**0.5) + 1
    for i in range(2, t):
        if n % i == 0:
            return False
    return True

def isPrime_simple(n:int) -> bool: 
    """
    isPrime_sqrt 함수와 동일한 알고리즘의 함수이지만, sqrt(n)까지 나누지 않고 쭉 나누는 함수입니다.
    성능 상 위 함수의 하위호환입니다.
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True




def isPrime_Eras(n:int) -> int:
    """
    에라스토테네스의 체를 이용하여 n 이하의 모든 소수를 구하는 방법입니다.
    소수 1개만 단일로 구할 때도 isPrime_sqrt 함수와 시간복잡도 차이가 적고,
    n 이하의 모든 소수를 구하는 경우, 이 방법이 가장 빠릅니다.
    """
    check = [True]*(n+1)
    for i in range(2, int((n+2)**0.5)+1):
        if check[i]:
            for j in range(i*2, n+1, i):
                check[j] = False
    return check[n]




def Miller_Rabin(n:int,_a:int) -> bool:
    """
    밀러-라빈 소수판정법을 이용한 방법입니다. 페르마의 정리의 역이 꽤 높은 확률로 성립한다는 성질을 이용합니다.
    소수가 담긴 리스트 A를 받아서, 그 원소에 있는 소수들에 대해서 밀러-라빈 판정법을 시행합니다.
    """
    d = (n-1) // 2
    while d % 2 == 0:
        if pow(_a,d,n) == n-1:
            return True
        d //= 2
    t = pow(_a,d,n)
    return True if t in (n-1, 1) else False

def isPrime_Miller(n:int, __E__ = [True] * 101) -> bool:
    for i in range(2, int(math.sqrt(102))+1):
        if __E__[i]:
            for j in range(i*2, 101, i):
                __E__[j] = False
    if n <= 1:
        return False
    if n <= 100:
        return True if __E__[n] else False
    for a in [2, 7, 61]:
        if not Miller_Rabin(n,a):
            return False
    return True
        


# Test input
# 24815323469403931728221172233738523533528335161133543380459461440894543366372904768334987264000000000000000000479
if __name__ == '__main__':
    num = int(sys.stdin.readline())
    print(isPrime_Miller(num))