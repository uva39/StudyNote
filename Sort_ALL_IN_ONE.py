import sys
RawData = [*eval("int(sys.stdin.readline().rstrip())," * int(input()))]
# N개의 data를 한 줄에 받아오는 코드

# TODO: 퀵정렬, 힙정렬, 기수정렬, 칵테일 정렬, 병합정렬, 셸 정렬 구현  and 파이썬 내장 정렬함수 사용법

# 선택정렬 - best: O(N^2) ~ worst: O(N^2)

# 1. 바꿀 데이터의 인덱스를 i라 하고, 0(맨 앞)으로 초기화한다.
# 2. O(n)의 시간복잡도로 배열에서 가장 작은 데이터를 찾은 뒤, arr[i]와 맞바꾼다.
# 3. 그 다음으로 작은 데이터를 선택해, arr[i+1]과 맞바꾼다.
# 4. i가 배열의 마지막에 도착할 때까지 반복한다.

def selection(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

# 삽입 정렬 - best: O(N) ~ worst: O(N^2)

# 정렬 과정에서 데이터가 들어가기에 적절한 위치를 찾은 뒤, 그 위치에 데이터를 삽입한다.
# 필요할 때만 위치를 바꾸기 때문에, "거의 정렬된 데이터"에서 매우 효율적이다.

# 1. 첫번째 데이터는 그 자체로 정렬되어있다고 가정한다.
# 2. 두번째 데이터부터 정렬된 데이터의 끝부터 처음까지 비교하면서 필요할 경우 삽입한다.
# 3. 마지막 데이터를 비교할 때까지 반복한다.

def insertion(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1): # j in (i, i-1, ... , 2, 1)
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

# 버블 정렬 - best: O(N^2) ~ worst: O(N^2)

# 서로 인접한 두 원소의 대소 관계를 비교해가며 정렬한다.

# 1. 서로 인접한 두 원소를 비교한 후, 큰 원소를 뒤로 보낸다.
# 2.