# 세그먼트 트리는 항상 Full Binary Tree의 형태이고, 만약 array의 길이가 2^N 꼴이면 Perfect Binary Tree의 형태가 된다.

# 1 - 세그먼트 트리의 재귀적 구현
# 2 - 세그먼트 트리의 비재귀적 구현

# 세그먼트 트리의 재귀적 구현
# 1. 쿼리에 맞는 세그먼트 트리를 생성하는 함수 init
# 2, 3. 쿼리에 맞게 세그먼트 트리는 업데이트하는 update 함수, 쿼리를 처리하는 query함수

# query가 구간합을 구하는 것일 때의 세그먼트 트리

def init(array, tree, node, start, end):
    # !query와 관계가 없는 부분!
    if start == end: # 종료 조건. start = end이면 leaf node이기에 대입하고 종료
        tree[node] = array[start]
        return
    # root node에서부터 반씩 구간을 쪼개면서 leaf node에 닿도록 재귀적으로 호출함

    mid = (start + end)//2
    init(array, tree, node*2, start, mid)
    init(array, tree, node*2 + 1, mid+1, end)

    # !Query와 상관있는 부분!
    # stack에 쌓인 재귀호출이 완료되면 leaf node부터 값이 대입되고, 상위의 노드들엔 두 자식노드의 값의 합을 더해서 대입한다.
    tree[node] = tree[node*2] + tree[node*2 + 1]

# array는 query를 처리하는 데엔 전혀 상관이 없다.(tree에 그 역할을 넘겨줌)
# node에 저장된 구간이 [start, end]이고 구간합을 구할 구간이 [left, right]일 때의 query함수
def query(tree, node, start, end, left, right):
    # left, right는 고정. 세그먼트 트리에서 검색할 때에 필요한 start, end만 바꿔가며 재귀 호출

    if left > end or right < start:
        return 0 # 구간합 범위 밖에 대해선 + 0 리턴. 곱하기라면 1일 것
    if left <= start and end <= right:
        return tree[node]
        # [start, end] 범위의 node가 [left, right]에 완전히 포함된다면 바로 리턴.
        # ex)