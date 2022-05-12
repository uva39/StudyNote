while True:
    Sentence = input()

    if Sentence == '.': # 종료조건
        break
    if not [1 for t in Sentence if t in '([])']: # 괄호가 아예 없을 때 yes처리
        print('yes')
        continue

    B = True
    Stack = []
    for x in Sentence:
        if x in '([': # 여는 괄호는 Stack에 추가
            Stack.append(x)
        elif x in ')]': # 닫는 괄호는 여는 괄호와 상쇄되어 없어지게 됨
            if len(Stack) == 0: # 여는 괄호가 아예 없는데 닫는 괄호가 들어오면 no처리
                B = False
                break
            t = Stack.pop() # 가장 최근에 들어온 열린 괄호를 Stack에서 제거 후, 이게 뭔지 t에 저장
            if t + x == '(]' or t + x == '[)': # t+x가 () 이나 [] 꼴이어야 함
                B = False
                break

    if len(Stack) != 0: # for문을 다 돌고도 열린 괄호가 남아있으면 no처리
        B = False

    print('yes') if B else print('no')
