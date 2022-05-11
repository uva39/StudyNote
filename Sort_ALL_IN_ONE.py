import sys
RawData = [*eval("int(sys.stdin.readline().rstrip())," * int(input()))]
# N개의 data를 한 줄에 받아오는 코드

# 이후의 시간복잡도 표기는 전부 Best - Average - Worst (최선 - 평균 - 최악) 순으로 표기한다.





# 타임소트(Time Sort): O(N) - O(NlgN) - O(NlgN)

# 파이썬의 기본 내장 정렬함수가 사용하는 알고리즘이 타임소트이다.
# 여러 정렬 알고리즘들을 짬뽕한 정렬방식이기에 이걸 처음부터 코드로 짜기보단, 사용법만 다룬다.

def time(arr):
    arr.sort(key=lambda x: x[0])
    # lambda x: x[0] -> x가 (12, 98, 23)같은 시퀀스일때, [0]인 12를 기준으로 해서 정렬을 수행한다는 뜻이다.
    arr.sort(key=lambda x: (x[0], x[1]))
    # lambda x: (x[0], x[1]) -> x[0]을 1순위, x[1]을 2순위로 고려해서 정렬한다. 인자가 늘어도 마찬가지의 뜻이다.



# 선택정렬(Selection Sort): O(N^2) - O(N^2) - O(N^2)

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



# 삽입 정렬(Insertion Sort): O(n) - O(n^2) - O(n^2)

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



# 버블 정렬(Bubble Sort): O(n) - O(n^2) - O(n^2)

# 서로 인접한 두 원소의 대소 관계를 비교해가며 정렬한다.
# 버블 정렬을 양방향으로 번갈아 수행한 것이 칵테일 정렬이다.

# 1. 서로 인접한 두 원소를 비교한 후, 더 큰 원소를 뒤로 보낸다.
# 2. 이걸 1 cycle동안 반복하면, 가장 큰 원소가 뒤로 가게 된다.
# 3. 따라서 이를 n회 반복하면, 데이터가 정렬된다.

def bubble(x):
    t = len(x)-1
    for i in range(t):
        for j in range(t-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]



# 칵테일 정렬(Cocktail Shaker Sort): O(n) - O(n^2) - O(n^2)

# 버블 정렬과 Big-O Notation의 시간복잡도 면에선 큰 차이가 없지만, 실제론 더 빠르게 동작한다.
# 최댓값으로 push하는 것만 반복했다면 버블 정렬이지만, 칵테일 정렬에선 최대, 최소로 원소들을 전부 push한다.
# 지금은 버블 정렬에 적용했지만, 칵테일 정렬의 아이디어 자체는 다른 정렬들에도 충분히 적용할 수 있어서, 범용성이 상당히 높다.

def cocktail(arr):
    a, b = 0, len(arr)
    swap = True  # 정방향 True / 역방향 False
    swapped = True  # 바뀌었는지
    while swapped:
        swapped = False

        if swap:  # 정방향
            for i in range(a, b):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True  # 바뀐게 있는지
            b = b - 1
            swap = False  # 방향전환
        else:  # 역방향
            for i in range(b - 1, a - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True  # 바뀐게 있는지
            a = a + 1
            swap = True  # 방향전환



# 퀵 정렬(Quick Sort): O(N) - O(NlgN) - O(N^2)

# O(NlgN) 알고리즘 중에서 대부분에 데이터에 대해 다른 O(NlgN) 알고리즘보다 빠르게 동작하고, 가장 보편적인 정렬 방법이다.
# 병합정렬(Merge Sort)과 퀵정렬 모두 분할정복(Divide and Conquer)방식과 재귀적인 알고리즘을 사용한다.
# 리스트 슬라이싱을 사용하여 구현할 경우엔, 슬라이싱이 새로운 리스트를 생성하기 때문에 공간복잡도 면에서 마이너스다.
# 게다가, 퀵정렬은 슬라이싱 없이 구현할 경우엔 추가 메모리를 필요로 하지 않아서 O(1)의 공간복잡도를 갖는다.
# 세부사항: https://www.daleseo.com/sort-quick/
# 단점으로는, 데이터가 이미 정렬된 상태에 가까울 수록 시간복잡도가 O(N^2)에 가까워진다는 점이 있다.

def quick(arr):
    # quick함수 안에 내부 함수 sort와 partition를 선언해서, 코드를 깔끔하게 정리한다.

    def sort(low, high):
        # 정렬 범위의 시작과 끝을 인수로 받는 재귀함수
        if high <= low:
            return # 종료조건

        mid = partition(low, high) # 정렬 범위의 시작과 끝을 인수로 받아, 분할 기준점을 반환하는 partition 함수
        # 분할된 범위에 대해 재귀적으로 퀵정렬 수행
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2] # 일단은 리스트의 가운데 값을 pivot으로 설정
        while low <= high:
            while arr[low] < pivot:
                # 정상적으로 pivot 왼쪽에 있으면서 pivot value보다 값도 작으면 OK.
                # 만약 pivot 왼쪽인데 안타깝게도 value가 pivot value보다 더 크면, pass하고 if로 이동
                low += 1
            while arr[high] > pivot:
                # 같은 논리
                high -= 1
            if low <= high:
                # 전체 while문의 조건을 다시 체크한 뒤, 안타까운 이 low와 high값을 서로 전환함.
                # while loop 2개를 돌며 arr[low] > arr[pivot] > arr[high]이 확정이 되었기에 서로 바꿔줘야 함.
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
                # 끝나면 다시 while loop을 돌러 감
        # low값은 증가하고, high값은 감소하다가.. 드디어 우리가 원하던 mid값이 low에 담기게 되었다.
        # 이전의 while loop에서 이걸 mid 이하 / mid / mid 초과 로 정렬이 완료되었다는 걸 기억하자.
        return low

    return sort(0, len(arr) - 1)



# 병합정렬(Merge Sort): O(NlgN) - O(NlgN) - O(NlgN)

# 퀵정렬과 마찬가지로 분할 정복 (Devide and Conquer) 기법과 재귀 알고리즘을 이용함.
# 세부 사항은 https://www.daleseo.com/sort-merge/

def merge(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge_sort(low, mid, high)

    def merge_sort(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))



# 힙 정렬(heap sort) - O(NlgN) - O(NlgN) - O(NlgN)

# 가장 단순한 O(NlgN) 알고리즘. 시간복잡도가 비교적 일정하기에 값이 매우 커질 때 특히나 유용하다.
# 대신, 정렬할 값의 개수가 적을 때엔 오히려 삽입정렬 등의 O(N^2) 알고리즘보다도 성능이 떨어진다.
# heapq 모듈을 사용하지 않는 경우엔 heapify(), heap class를 따로 구현해야한다.

import heapq
def heap(arr):
    l = len(arr)
    H = []
    for i in range(l):
        heapq.heappush(H, arr[i])
    for i in range(l):
        arr[i] = heapq.heappop(H)

# TODO: 기수정렬, 셸 정렬 구현
