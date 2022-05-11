word=input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
I = [-1 for i in range(len(alphabet))]
for j, x in enumerate(alphabet):
    if x in word:
        I[j] = word.index(x)

for i in I:
    print(i,end=' ')