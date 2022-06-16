# 학번 입력해서 코드 시작
# agent가 기계 만들고 (노가다 코드)
# 기계의 중앙에 agent가 있고
# 무한루프로 agent.collect를 하고,
# agent의 슬롯1을 무한루프 안에서 체크
# 슬롯1이 음식이면 -> 실행, 아니면 -> 아이템 그대로 되보내기
# 데이터를 받아서 {음식:포만감} 딕셔너리에서 포만감 검색
# 포만감 * 음식 개수 만큼 뼛가루
def make_machine():
    # 기계 만들기(블록 설치) U자형
    # agent를 중앙에 배치
    # 반블록 안팎에 설치
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

        for i in range(1, 28): # 인벤토리 초기화
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

# K = [COOKED_BEEF, COOKED_CHICKEN, COOKED_FISH, COOKED_MUTTON]
# V= []

# def make_machine():
#     # 좌표 입력
#     loc = player.position()
#     x = loc.get_value(Axis.X) + 3
#     y = loc.get_value(Axis.Y)
#     z = loc.get_value(Axis.Z)


#     # 테두리(뼈대) 만들기
#     for i in range(5):
#         blocks.fill(BLACK_WOOL if i%2 == 0 else WOOL, world(x-2, y+i, z-2), world(x+2, y+i, z+2))
#     blocks.fill(AIR, world(x-1, y+1, z-1), world(x+1, y+4, z+1))

#     # 나선형 외부계단 만들기
#     for i in range(1, 6):
#         m_place(QUARTZ_SLAB, world(x-3, y+i-1, z+3-i))
#         m_place(QUARTZ_SLAB, world(x+3, y+i-1, z-3+i))
#         m_place(QUARTZ_SLAB, world(x-3+i, y+i-1, z-3))
#         m_place(QUARTZ_SLAB, world(x+3-i, y+i-1, z+3))

#     # 나선형 내부계단 만들기
#     m_place(QUARTZ_SLAB, world(x-1, y+1, z-1))
#     m_place(BLOCK_OF_QUARTZ, world(x, y+1, z-1))
#     m_place(QUARTZ_SLAB, world(x+1, y+2, z-1))
#     m_place(BLOCK_OF_QUARTZ, world(x+1, y+2, z))
#     m_place(QUARTZ_SLAB, world(x+1, y+3, z+1))
#     m_place(BLOCK_OF_QUARTZ, world(x, y+3, z+1))
#     m_place(QUARTZ_SLAB, world(x-1, y+4, z+1))
#     m_place(BLOCK_OF_QUARTZ, world(x-1, y+4, z))

#     # agent 위치 초기화
#     agent.teleport(world(x, y+1, z), WEST)

# def m_place(b, coord):
#     blocks.fill(b, coord, coord)

# def check(_item):
#     _a = ''
#     for i in range(len(K)):
#         if K[i] == _item:
#             return
#     return False

# def on_on_chat():
#     make_machine()
#     while True:
#         loops.pause(1000)
#     agent.collect_all()
#     item = agent.get_item_detail(1)  # slot1의 아이템 저장

#     for i in range(1, 28): # 인벤토리 초기화
#         agent.set_item(AIR, 1, i)


#     if item in K:  # 입력받은 아이템이 음식일 경우
#         hunger = V[item]
#         agent.drop_all(FORWARD)
#         # 아이템뿌리기(뼛가루, (item개수 * hunger) // 10)
#     else:  # 음식이 아닐 경우
#         print("고기류 음식을 입력해주세요")

# player.on_chat("2022174063", on_on_chat)

agent.collect_all()