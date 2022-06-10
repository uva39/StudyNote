import sys
import heapq
from collections import defaultdict

fi = sys.stdin.readline

def sol(queue):
    answer = []
    num_dict = defaultdict(int)
    min_heap = []
    max_heap = []
    for o in range(queue):
        q, num = fi().split()
        num = int(num)
        if q == 'I':
            num_dict[num] += 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if num == 1:
                while max_heap:
                    max_num = -heapq.heappop(max_heap)
                    if num_dict[max_num] != 0:
                        num_dict[max_num] -= 1
                        break
            else:
                while min_heap:
                    min_num = heapq.heappop(min_heap)
                    if num_dict[min_num] != 0:
                        num_dict[min_num] -= 1
                        break

    while max_heap and num_dict[-max_heap[0]] == 0: heapq.heappop(max_heap)
    while min_heap and num_dict[min_heap[0]] == 0: heapq.heappop(min_heap)

    if not max_heap:
        print('EMPTY')
    else:
        print(-max_heap[0], min_heap[0])


T = int(fi())
for _ in range(T):
    k = int(fi())
    sol(k)