# 스택을 활용해서 괄호가 있는 문장이 괄호가 적절히 배치되었는지 판정하는 문제임.
# 나는 그냥 deque 써봄. 진짜 몰라서 써보긴 했는데, 없어도 코드 속도 차이는 없을듯?
# TODO: 코드를 더 간결하게 쓰기. 이미 정답 코드이긴 함

from collections import deque

while True:
    Sentence = input()
    B = True

    if Sentence == '.':
        break

    Temp = [1 for t in Sentence if t in '([])']
    if len(Temp) == 0:
        print('yes')
        continue

    queue = deque()
    for x in Sentence:
        if x in '([':
            queue.append(x)
        elif x in ')]':
            if len(queue) == 0:
                B = False
                break
            t = queue.pop()
            if t + x == '(]' or t + x == '[)':
                B = False
                break

    if len(queue) != 0:
        B = False

    if B:
        print('yes')
    else:
        print('no')
