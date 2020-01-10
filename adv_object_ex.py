# 객체의 이해

# global 영역 -> 내부에 있는 어디서든 접근 가능
global_a = 1
global_b = "Global"

# 객체 심볼 테이블의 영역
# Local 영역
# Enclosed 영역
# Global 영역 (해당 파이썬 모듈 내)
# Built-in 영역 (파이썬 실행 환경)

def func():
    local_a = 2
    local_b = "Local"
    print(locals()) # 로컬 영역의 심볼 테이블 확인

def symbol_table():
    print("GLOBAL:", globals())     # 글로벌 영역의 심볼 테이블 확인
    print("Type of globals", type(globals))

    func()

    # symbol table은 dict
    print("global_a in global scope?", "global_a" in globals())

    # 각각의 영역별로 심볼 테이블을 별도 관리하지 있다 (!중요!)
    # 객체에 접근할 때 순서는 local -> enclosed -> global -> built-in 순으로 검색을 한다 (!중요!)

def object_id():
    # 불변형 자료 -> 값이 같으면 같은 객체로 취급
    # 가변형 자료 -> 값이 같아도 다른 객체로 취급
    x = 10
    y = 10

    print("x의 주소:", hex(id(x)))  # id()함수 -> 객체 주소 확인
    print("y의 주소:", hex(id(y)))

    # x의 주소와 y의 주소가 같은가?
    print("x의 주소는 y의 주소와 같은가?", id(x) == id(y))
    # 두 객체의 주소가 같다 -> 같은 객체

    # == vs is
    # ==: 값의 비교 -> 동질성의 비교
    # is: 주소의 비교 -> 동일성의 비교
    print("x == y:", x == y)  # 값의 비교
    print("x is y:", x is y)  # 주소의 비교

    # 불변 자료형의 경우
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]

    print("lst1 == lst2?", lst1==lst2)
    print("lst1 is lst2?", lst1 is lst2)
    # lst1, lst2 -> 같은 데이터를 가지고 있지만 다른 객체임

def object_copy():
    """
    객체의 복제
    -> 유의 : 특히 복합 객체의 경우
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    x = [a, b, 100]

    # 레퍼런스 복제 -> 단순 주소를 복제
    y = x
    print("x의 주소:", hex(id(x)))
    print("y의 주소:", hex(id(y)))

    print("x is y?", x is y)

    # 얕은 복제
    # [:] -> 전체 -> 새로 할당
    # .copy 메서드
    # copy 모듈의 copy 메서드
    import copy # copy 모듈의 사용
    y = copy.copy(x)
    print("x is y?", x is y)

    print("x:", x)
    print("y:", y)

    # x와 y는 별개의 객체지만 내부의 자료 a, b는 동일 주소
    print("x[0] is y[0]?", x[0] is y[0])
    # 복합 객체의 얕은 복제는 문제를 일으킬 수 있다
    y[0][0] = 100
    print("x:", x)

    # 복합 자료형의 경우는 내부 데이터도 새로 복제해서 다시 할당해야 한다
    # 깊은 복제 (중요)
    y = copy.deepcopy(x) # 깊은 복제
    print("x:", x)
    print("y:", y)

    y[1][0] = 100
    print("x:", x)


# symbol_table()
# object_id()
object_copy()