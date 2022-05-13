import statistics

n = int(input())
K = [0]*n

for i in range(n):
    K[i] = int(input())

K.sort() # N개의 데이터를 입력받고 정렬

print(round(sum(K)/len(K))) # 평균(Mean)을 정수가 되도록 반올림하여 출력

print(K[len(K)//2]) # 중앙값(Median)

mode = statistics.multimode(K) # 최빈값(Mode)
print(mode[1] if len(mode) > 1 else mode[0])

print(max(K) - min(K)) # 범위(최댓값 - 최솟값)
