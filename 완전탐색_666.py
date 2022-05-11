n = int(input())

array = [i for i in range(1,n*1000) if '666' in str(i)]
# List Comprehension을 하면서 Gravity Sort까지 1 + 1 으로 실행해줌
print(array[n-1])

# TODO: EXAMPLE FOR GRAVITY SORT

# import sys
# print("First: 몇 번 입력할지, Next: 정렬되지 않은 수들")
#
# t = int(input())
# A = [0]*100001
#
# for i in range(t):
#     A[int(sys.stdin.readline())] += 1
#
# for i in range(len(A)):
#     if A[i] != 0:
#         print(i)