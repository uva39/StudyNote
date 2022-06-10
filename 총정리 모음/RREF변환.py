from icecream import  ic

def trans_row(row1, row2): # 기본 행 연산 - 1
    NewMat[row2 - 1], NewMat[row1 - 1] = NewMat[row1 - 1], NewMat[row2 - 1]

# def multiply_row(row, coeff): # 기본 행 연산 - 2
    # TODO 일단 일괄적으로 p에 coefficient를 곱하고, 2/2같은 것들이 생길 수 있으니 마지막에 모든 원소를 약분 처리한다
    # for x in NewMat[row-1]:
    #     c = coeff
    #     if c < 0:
    #         c = -c


def make_RREF(row):
    RowPivot = NewMat[row-1][row-1]
    for i in range(m): # TODO: 1 0 0; 0 1 0; 0 0 1 일케 만들기 전, '1'처럼 normalize를 일단 해주기
        NewMat[row-1][i][0] = 1


def mat_reverse_analyze(row):
    pass


# Input, Initialize, Analyze
def mat_analyze(row):
    for i, x in enumerate(MAT[row]): # x : matrix의 원소. ex: -7/5, 5, -3, 1/3
        # PLAN: 문자열의 첫 원소가 '-'인지 판별, 맞으면 counting한 뒤 없애고, 마지막에 음수로 변환
        # 그러니 이 코드 이후의 문자열은 '전부' 양수임.
        # '/'이 문자열에 있으면 분수로 인식. 분자, 분모 = p, q로 설정 후 튜플로 삽입.

        Sign = True # 마이너스 부호 삭제
        if x[0] == '-':
            Sign = False
            y = ''.join(x[1:])
        else:
            y = ''.join(x[:])

        if '/' in x:
            p, q = map(int, y.split('/'))
        else:
            p = int(y)
            q = 1
        NewMat[row][i] = [+Sign, p, q]

n, m = map(int, input().split())
MAT = [['0' for _ in range(m)] for __ in range(n)]
NewMat = [['0' for _ in range(m)] for __ in range(n)]
for i in range(n):
    MAT[i] = input().split()
    mat_analyze(i)
# Input, Initialize, Analyze

ic(NewMat)
# TODO: 입력은 항상 기약분수 형태이기에 약분할 필요는 없음. 하지만, 출력하기 전에는 약분이 필요.
