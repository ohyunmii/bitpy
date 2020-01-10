# 흐름 제어(flow control)
# 1. 조건문
# 2. 반복문
# 프로그램의 흐름을 제어

# if ~ elif ~ else
def if_statement():
    # 금액을 입력받고
    # 10000원 이상이면 by taxi
    # 2000 ~ 10000이면 by bus
    # 그 미만이면 on foot을 출력
    money = int(input("얼마 가지고 있어?"))

    message = "" # 메시지 출력
    """
    # 조건 판별
    if money >= 10000: # 첫번째 조건의 판별
        message = "by taxi"
    elif money >= 2000: # 추가 조건 판별
        message = "by bus"
    else: # 위 조건 중 만족하는 것이 없을 때 처리
        message = "on foot"
    """

    # 중첩 if: if문은 중첩할 수 있다
    if money < 2000:
        message = "on foot"
    else: #
        if money >= 10000:
            message = "by taxi"
        else:
            message = "by bus"

    print("이동 방법:", message)

def if_expr():
    """
    조건 판별식
    -> 조건 판별을 계산식 내부에서 수행하는 방법
    """
    money = int(input("얼마 가지고 있어? "))
    message = "by taxi" if money >= 10000  else "by bus" \
                                        if money >= 2000 else "on foot"

    print("이동방법:", message)

def for_ex():
    """
    for문 연습
    Syntax: for 객체 in 순차형
    """

    # 1. 1~100 정수 합산
    result = 0
    for num in range(1, 101): # 1~100까지
        result += num
    else:  # 루프 정상 종료시에만 실행
        print("합산 완료")

    print("결과:", result)

    # 2. 구구단 만들기
    # 중첩 for 루프 사용
    for dan in range(2, 10): # 2~9까지
        print("==", dan, "단 ==")
        for num in range(2, 10):
            print("{} * {} = {}".format(dan, num, dan*num))

    # 3. 삼각형 그리기
    for num in range(1, 6): # 1~5까지
        for i in range(1, num+1):
            print("*", sep="")
        else:
            print()

    # 4. 삼각형 그리기 풀이 2
    for num in range(1, 6):
        print("*" * num)

def list_comp():
    """
    리스트 내포
    Syntax: [표현식 for 객체 in 순차형 if 추출 조건]
    """

    nums = list(range(1, 11))
    print("nums:", nums)
    # nums 리스트의 각 요소를 제곱한 새로운 리스트 생성
    result = []
    for num in nums:
        result.append(num**2)
    print("result:", result)

    # 리스트 내포방식
    result = [num ** 2 for num in nums]
    print("result(comp):", result)

    # 문자열 리스트
    words = ["a", "as", "bat", "cat", "dove", "python"]
    # 문자열 리스트 중에서 길이가 3글자 이상인 단어만 별도 리스트로 생성
    result = [ word.upper() for word in words if len(word) >= 3]
    print("words(comp):", result)

    # 1 ~ 100 사이의 수열 중에서 짝수 리스트만 추출
    evens = [num for num in range(1, 101) if num % 2 == 0]
    print("Evens:", evens)

def set_comp():
    """
    SET 내포
    Syntax: {표현식 for 객체 in 순차형}
    """

    words = ["a", "as", "bat", "cat", "dove", "python"]
    # 문자열의 길이를 set으로 저장
    lens = { len(word) for word in words }
    print(lens)

def dict_comp():
    """
    사전의 내포
    Syntax: {키 표현식: 값 표현식 for 객체 in 순차형}
    """

    words = ["a", "as", "bat", "cat", "dove", "python"]
    # 단어를 키로, 단어의 길이를 값으로 가지는 사전을 생성
    len_dct = {word:len(word) for word in words}
    print(len_dct)

def while_ex():
    """
    while문 연습
    # 반복 조건을 확인하기 위한 변수 객체를 개발자가 직접 제어
    # 무한 루프에 빠질 위험이 있으므로 주의
    # 의도적으로 무한루프를 만들기도 한다
    """

    # 연습 1: 1~100까지 수의 합
    num, result = 1, 0
    while (num < 100):
        result += num;
        num += 1 # 주의 -> 잘못하면 무한 루프에 빠질 수 있음
    else:
        print("합산 완료") # 루프가 정상종료 되었을 경우 실행

    print("합산 결과:", result)


    # 연습 2: 구구단
    dan = 2
    while (dan <= 9):
        print(dan, "단")
        num = 2
        while(num <= 9):
            print("{} * {} = {}".format(dan, num, dan * num))
            num += 1
        dan += 1 # 반복 조건 변수 제어
    else:
        print("구구단 정상 종료")

    # 연습 3: 1 ~ 100까지 while 루프를 돌리며 3의 배수만 출력 using continue
    num = 0
    while(num <=100):
        num += 1
        # 체크
        if(num%3 != 0): # 3의 배수가 아닌 경우
            continue    # 남아있는 명령 수행하지 않고 다음번 루프
        print(num, "는 3의 배수")
    else:
        print("루프 정상 종료")

    # 연습 4: 13과 17로 동시에 나눠지는 가장 작은 수
    num = 17
    while True:
        if num % 13 == 0 and num % 17 == 0:
            break
        num += 1
    else:
        print("그런 수 없어요.")  # 이 블록은 실행되지 않음. 루프에서 break로 나오기 때문.

    print("최소의 수:", num)

if __name__ == "__main__":
    # if_statement()
    # if_expr()
    # for_ex()
    # list_comp()
    # set_comp()
    # dict_comp()
    while_ex()