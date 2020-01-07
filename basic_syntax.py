# This file covers basics of python syntax.

def func():
    # 블록은 들여쓰기가 시작되는 곳에서 시작되고, 들여쓰기가 끝나는 곳에서 끝난다.
    pass # 블록은 비어있으면 안됨. 구현부가 없을 경우에도 pass를 작성

def func2():
    print("Hello", "Python", sep=",", end="!\n");

# Arithmetic Operator
def arith_oper():
    print("======= Arithmetic Operator")
    # +, -, *, /
    print("7/5? ", 7/5)                 # int/int -> if there is remainder, int casts into float
    print("7/5 ", 7//5)                 # 7/5의 몫
    print("remainder of 7/5:", 7%5)     # 7/5의 나머지

    # divmod() -> 나눗셈과 나머지
    print("divmod(7,5):", divmod(7,5))
    print("7 나누기 5의 몫: ", divmod(7,5)[0])
    print("7 나누기 5의 나머지: ", divmod(7, 5)[1])

    # Power(제곱): **
    print("2의 3승: ", 2**3)             # 2^3
    print("pow(2,3):", pow(2,3))         # exactly same as **

# Relational Operator(비교 연산자)
def rel_oper():
    print("======== 비교(관계) 연산")
    # >, >=, <, <=
    # == (같다), != (같지 않다)
    # 결과는 논리값 (True or false)
    print("1 > 3?", 1 > 3)
    print("6 equals 9?", 6 == 9)
    print("6 not equals 9?", 6 != 9)

    # 복합 관계식
    a = 6
    # a가 0~10 사이에 위치하는가?
    # 조건 1: a > 0
    # 조건 2: a < 10
    print(a, "가 0 ~ 10 사이?", a > 0 and  a < 11)
    print(a, "가 0 ~ 10 사이?", 0 < a < 11)             # 복합 관계식 표현

    # 수치 자료형 이외의 자료형의 대소 비교
    print("문자열의 대소:", "abcd" < "abd")       # 문자열 크기 비교 아님
    print("리스트의 대소:", [1,2,3] < [1,2,4])
    print("튜플의 대소 비교:", (1,2,3) < (1,2,4))


# 변수 할당
def variable_ex():
    print("====== 변수의 할당")
    # 변수 선언 작업은 없다
    # 문자, 숫자, _의 조합 -> 숫자로 시작하면 안됨
    # .py 파일의 이름도 변수 명령 규칙에 따라 작성하는 것이 좋음
    # 예약어는 사용할 수 없음
    import keyword
    print("예약어 목록:", keyword.kwlist)

    # 변수 치환문 (치환 연산자 = ), 선언은 없음
    a = 10     

    # 여러 변수의 동시 할당. 단, 좌변의 변수 갯수 == 우변의 값 갯수
    b, c = 20, 30

    # 같은 객체를 여러 변수에 동시 할당
    d = e = f = 40
    print(d, e, f)

    # 동적 타이핑
    g = 2020
    print("g: ", g, type(g))

    g = "Python" # 다른 타입의 객체를 재할당
    print("g: ", g, type(g))

    # isinstance(객체, 점검할 타입)
    if isinstance(g, str):
        print(g, "는 문자열.")
    else:
        print(g, "는 문자열이 아님")

    # 여러 개의 타입 중 하나인지 확인
    h = 2020
    if isinstance(h, (int, float, complex)):     # int이거나 float이거나 복소수인지
        print(h, "는 산술 계산이 가능함")
    else:
        print(h, "는 산술 연산 불가")

if __name__ =="__main__":
    # func()
    # func2()
    # arith_oper()
    # rel_oper()
    variable_ex()


