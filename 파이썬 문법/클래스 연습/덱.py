from sys import stdin
fi = stdin.readline


# Class 연습 - 1. 덱(deck) 만들기
class deck(list):
    def __init__(self) -> None:
        super().__init__(self)
        self.arr = list()

    def push_front(self, X):
        self.arr.insert(0, X)

    def push_back(self, X):
        self.arr.append(X)

    def pop_front(self, _):
        if self.arr:
            print(self.arr.pop(0))
        else:
            print(-1)

    def pop_back(self, _):
        if self.arr:
            print(self.arr.pop())
        else:
            print(-1)

    def size(self, _):
        print(len(self.arr))

    def empty(self, _):
        print(0 if self.arr else 1)

    def front(self, _):
        if self.arr:
            print(self.arr[0])
        else:
            print(-1)

    def back(self, _):
        if self.arr:
            print(self.arr[-1])
        else:
            print(-1)


T = int(fi())
D = deck()

_l1 = ("push_front", "push_back", "pop_front", "pop_back", "size", "empty", "front", "back")
_l2 = (D.push_front, D.push_back, D.pop_front, D.pop_back, D.size, D.empty, D.front, D.back)

FuncBox = dict(zip(_l1, _l2))

for i in range(T):
    oper = fi().rstrip()
    t = None
    if ' ' in oper:
        oper, t = oper.split()
        t = int(t)

    f = FuncBox[oper]
    f(t)