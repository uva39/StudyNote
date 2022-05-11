word = input()
C = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
l, t = 0, []
for i in range(len(word)):

    if i in t:
        continue

    if i < len(word) - 2 and word[i]+word[i+1]+word[i+2] in C: # dz= 분류
        t.append(i+1)
        t.append(i+2)
        l += 1
    elif i < len(word) - 1 and word[i]+word[i+1] in C: # 두 글자 크로아티아 알파벳 분류
        t.append(i+1)
        l += 1
    else:
        l += 1
    
print(l)