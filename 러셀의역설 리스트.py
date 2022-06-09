# 자기 자신을 포함하는 리스트 'a' 생성
a = [1]
a.append(a)

# 자기 자신을 포함하는 리스트 'b' 생성
b = [1]
b.append(b)

# a[1]은 a이므로, 이걸 몇 번이고 반복하던지, 계속 a가 나온다.
# b에 대해서도 마찬가지일 것이다.
print(f'{a = }')
print(f'{a[1] = }')
print(f'{a[1][1] = }')
print(f'{a[1][1][1] = }')

# a와 a[1], 또는 이보다 더 깊이 인덱싱했을 때에도 데이터의 주소가 같은지 볼때 같다고 나온다.
# 이는 사실 당연한데, 리스트에 대해서 b = a를 했을 때 b는 a를 복사한 리스트가 아니라, a와 완전히 동일한 주소를 갖는 a의 레퍼런스 꼴이라는 것을 생각하면
# a.append(a)가 a[1] = a로 취급될 때, 저렇게 됨을 이해할 수 있다.
print(f'{a is a[1] = }')
print(f'{a is a[1][1] = }')
print(f'{a[1] is a[1][1] = }')

# b는 a와 다른 주소를 갖는다. 따라서 주소에 대해서 비교할 때엔 False가 출력된다.
print(f'{a is b} =')

# 하지만, 값을 비교할 경우엔 파이썬의 리스트 비교 알고리즘의 동작방식의 문제로 오류가 발생한다.
# 파이썬은 리스트끼리 비교를 수행할 때에 각 리스트의 모든 원소들이 서로 같은지 검사한다.
# 이는 중첩된 리스트에서도 동일하게 작용하는데, 이때 재귀를 사용한다. 그런데, 파이썬은 재귀 최대 깊이가 1000으로 제한되어있다.
# 그렇기에, 무한대로 리스트가 중첩된 이런 리스트에 대해서는 비교 연산 수행 시 에러가 발생한다.
try:
    print(f'{a == b} =')
except Exception as error:
    print(error)

# 이와 별개로, 파이썬에선 부울 연산이 short-circuit을 사용하듯이, a == a를 연산할 때에, 이미 a is a == True이므로, 비교를 수행하지 않는다.
print(f'{a == a = }')
# 또, a는 무한대로 중첩된 리스트이기에
# b = dict(zip(tuple(a), range(len(a))))