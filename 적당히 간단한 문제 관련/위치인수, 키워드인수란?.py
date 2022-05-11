def custom_print(*args, **kwargs):
    print(*args, **kwargs)

def personal_info(name, **kwargs):
    print(name)
    print(**kwargs)

custom_print('h','e','l','l','o', sep='MIKU\n', end='MIKU\n')

personal_info('홍길동')
personal_info('홍길동', age=30, address='서울시 용산구 이촌동')
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})

# *args는 가변 인수를 입력받을 때 사용한다. print문에서 여러 개를 입력받는 것과 같은 이치.
# **kwargs는 가변 키워드 인수를 입력받을 때 사용한다.
# TIP: **kwargs에 딕셔너리의 value를 입력받을 수 있다. 만약 *kwargs 형태로 썼다면 딕셔너리의 key를 입력받는 것이다.
