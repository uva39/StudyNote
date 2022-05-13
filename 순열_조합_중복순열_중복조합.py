from itertools import *

N = int(input())
Data = list(range(1, N+1))
print(Data)
R = int(input())

# 파이썬 내장 모듈을 통한 순열, 조합, 중복순열, 중복조합의 구현
def by_module(n, r):
    print(f"{n} 순열(Permutation) {r}")
    print(*permutations(Data, r))

    print(f"{n} 조합(Combination) {r}")
    print(*combinations(Data, r))

    print(f"{n} 중복순열(Product) {r}") # 중복순열 = 집합에서의 데카르트 곱이다.
    print(*product(Data, repeat=r))

    print(f"{n} 중복조합(Combinations with replacement) {r}")
    print(*combinations_with_replacement(Data, r))




# 제너레이터를 이용해서 조합 구현
# 제너레이터를 이용해서 조합을 구현할 경우, itertools의 조합보다 시간이 대략 10배 정도 더 걸린다.
def generator_nCr(array, r):
     for i in range(len(array)):
        if r == 1:  # 종료 조건
            yield [array[i]]
        else:
            for NEXT in generator_nCr(array[i + 1:], r - 1):
                yield [array[i]] + NEXT

print(*generator_nCr(Data, R))


# 제너레이터를 이용한 중복조합. 아주 조금만 바꾸면 조합이 중복조합이 된다는 장점이 있다.
def generator_nHr(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            # array[i+1: ] -> array[i: ] 변경
            for NEXT in generator_nHr(array[i:], r - 1):
                yield [array[i]] + NEXT

print(*generator_nHr(Data, R))