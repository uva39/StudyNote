# 학번 입력해서 코드 시작
# agent가 기계 만들고 (노가다 코드)
# 기계의 중앙에 agent가 있고
# 무한루프로 agent.collect를 하고,
# agent의 슬롯1을 무한루프 안에서 체크
# 슬롯1이 음식이면 -> 실행, 아니면 -> 아이템 그대로 되보내기
# 데이터를 받아서 {음식:포만감} 딕셔너리에서 포만감 검색
# 포만감 * 음식 개수 만큼 뼛가루
def make_machine():
    # 기계 만들기(블록 설치)
    # agent를 중앙에 배치
    pass


Foods = dict(zip([아이템이름], [포만감]))  # 아이템이름:포만감 쌍

class_number = input()
_num = '20221186'
if class_number == _num:
    print("아이템을 천천히 입력하세요.")
    make_machine()
    while True:
        loops.pause(1000)  # 1초마다 loop
        agent.collect()
        item = agent.get_item_detail(1)  # slot1의 아이템 저장
        if item == AIR: # 아이템을 안받았을 경우
            continue

        for i in range(1, 37): # 인벤토리 초기화
            agent.set_item(0, 1, i)

        if item in Foods:  # 입력받은 아이템이 음식일 경우
            hunger = Foods[item]
            아이템뿌리기(뼛가루, (item개수 * hunger) // 10)
        else:  # 음식이 아닐 경우
            print("고기류 음식을 입력해주세요")
            continue
else:
    print("학번이 일치하지 않습니다.")

# TODO: make_machine() 함수 *HARD*
# TODO: Foods 딕셔너리 (기호에 따라서 고기류만 해도 됨) *HARD*
# TODO: 여기에 의사코드(sudo code)로 입력한 거 다 실제 코드로 고치기
# TODO: 아이템뿌리기 함수 쓰기
# TODO: 실제로 collect함수가 생각대로 동작하는지, agent.set_item(0, 1, 1)이 제대로 작동하는지