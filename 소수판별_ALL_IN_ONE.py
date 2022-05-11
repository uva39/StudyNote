import math
import sys



# NORMAL RANGE OF PRIME




def isPrime_sqrt(n): # import math
    t = int(math.sqrt(n)) + 1
    for i in range(2, t):
        if n % i == 0:
            return False

    return True




# SIMPLE




def isPrime_simple(n): 
    for i in range(2, n):
        if n % i == 0:
            return False

    return True





# MANY PRIMES




def isPrime_Eras(n): # import math
    check = [True] * n+1
    for i in range(2, int(math.sqrt(n+2))+1):
        if check[i]:
            for j in range(i*2, n+1, i):
                check[j] = False
    return check







# ULTRA MANY , LARGE PRIMES









def Miller_Rabin(n,a): # import math, import sys
    d = (n-1) // 2
    while d % 2 == 0:
        if pow(a,d,n) == n-1:
            return True
        d //= 2
    t = pow(a,d,n)
    return True if t == n-1 or t == 1 else False

def isPrime_MR_Eras(n):
    if n <= 1:
        return False
    if n <= 100:
        return True if E[n] else False
    # over is not Miller_Rabin Test. It's Erastotenes.
    for a in A:
        if not Miller_Rabin(n,a):
            return False
    return True
        

# non-function initial setting
E = [True] * 101
for i in range(2, int(math.sqrt(102))+1):
    if E[i]:
        for j in range(i*2, 101, i):
            E[j] = False
# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
# in usual, A = [2,7,61] is best.
A = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

# Test input for Super Big Integer. Is following number prime?
# 24815323469403931728221172233738523533528335161133543380459461440894543366372904768334987264000000000000000000479
num = int(sys.stdin.readline())
print(isPrime_MR_Eras(num))