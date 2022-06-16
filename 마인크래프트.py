# 음식 이름 - 허기 값 쌍
K = [COOKED_BEEF, COOKED_CHICKEN, COOKED_FISH, COOKED_MUTTON, COOKED_PORKCHOP, COOKED_RABBIT,
     COOKED_SALMON, RAW_BEEF, RAW_CHICKEN, RAW_FISH, RAW_MUTTON, RAW_PORKCHOP, RAW_RABBIT,
     RAW_SALMON, ROTTEN_FLESH, SPIDER_EYE, TROPICAL_FISH]
V = [8, 6, 6, 6, 8, 5, 6, 3, 2, 2, 2, 3, 3, 2, 4, 2, 1]


def make_machine():  # 기계 생성 함수
    # 좌표 입력
    loc = player.position()
    x = loc.get_value(Axis.X) + 3
    y = loc.get_value(Axis.Y)
    z = loc.get_value(Axis.Z)

    # 테두리(뼈대) 만들기
    for i in range(5):
        blocks.fill(BLACK_WOOL if i % 2 == 0 else WOOL, world(x - 2, y + i, z - 2), world(x + 2, y + i, z + 2))
    blocks.fill(AIR, world(x - 1, y + 1, z - 1), world(x + 1, y + 4, z + 1))

    # 나선형 외부계단 만들기
    for i in range(1, 6):
        m_place(QUARTZ_SLAB, world(x - 3, y + i - 1, z + 3 - i))
        m_place(QUARTZ_SLAB, world(x + 3, y + i - 1, z - 3 + i))
        m_place(QUARTZ_SLAB, world(x - 3 + i, y + i - 1, z - 3))
        m_place(QUARTZ_SLAB, world(x + 3 - i, y + i - 1, z + 3))

        # 뼛가루 출구 생성
    m_place(WATER, world(x + 1, y + 1, z + 1))
    m_place(WOODEN_TRAPDOOR, world(x - 2, y + 1, z - 1))
    m_place(WOOL, world(x - 2, y - 2, z - 1))
    m_place(REDSTONE_TORCH, world(x - 2, y - 1, z - 1))

    # agent 위치 초기화
    agent.teleport(world(x, y + 1, z), WEST)

    # agent 인벤토리 초기화
    for i in range(1, 28):
        agent.set_item(BEDROCK, 64, i)
    agent.set_item(AIR, 1, 1)


# 블록을 한 칸 설치하는 함수
def m_place(b, coord):
    blocks.fill(b, coord, coord)


# 입력이 음식인지 확인하는 함수
def check(_item):
    for i in range(len(K)):
        if K[i] == _item:
            return V[i]
    return 0


# 메인 함수
def on_on_chat():
    make_machine()  # 기계 생성
    while True:
        loops.pause(100)

        # 아이템 입력 저장
        agent.collect_all()
        item = agent.get_item_detail(1)
        count = agent.get_item_count(1)
        agent.set_item(AIR, 1, 1)

        # 입력이 음식일 경우
        c = check(item)  # 아이템의 허기량

        if c:
            # 허기량이 0이 아니면(음식이면)
            # agent의 인벤토리를 초기화한 뒤, 정해진 개수의 뼛가루로 채움

            # 초기화
            for i in range(1, 28):
                agent.set_item(AIR, 64, i)

            amount = c * count  # 출력할 뼛가루의 개수
            slot = 1  # 현재 슬롯
            while True:
                # 뼛가루의 개수가 64개 이상인 경우, 현재 슬롯을 꽉 채우고 다음 슬롯으로 이동
                if amount >= 64:
                    agent.set_item(BONE_MEAL, 64, slot)
                    slot += 1
                    amount -= 64
                # 64개 미만이면, 현재 슬롯을 남은 뼛가루로 꽉 채우고 종료
                else:
                    agent.set_item(BONE_MEAL, amount, slot)
                    break

            # 뼛가루 출력
            agent.drop_all(FORWARD)
            return


player.on_chat("2022174063", on_on_chat)
