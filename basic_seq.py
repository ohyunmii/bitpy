# 순차형의 객체들
# range, enumerate, zip

def using_range():
    """
    range: 범위 객체
        실제 데이터는 필요할 때 하나씩 생성한다
        그 자체가 순차 객체다 -> 길이, 인덱싱, 슬라이싱, 포함여부 등을 확인
    """

    # 인자값이 1개 -> 끝 경계
    seq = range(10) # 0부터 9까지 (주의)
    print(seq, type(seq))
    # 실제 데이터 확인
    print("numbers in seq:", list(seq))

    # 인자값이 2개 -> 시작, 끝경계
    seq2 = range(2, 10) #2부터 9까지
    print(seq2, type(seq2))
    print("numbers in seq2:", list(seq2))

    # 인자값이 3개 -> 시작, 끝경계, 간격
    seq3 = range(2, 10, 2) # 2부터 9까지 간격 2
    print(seq3, type(seq3))
    print("numbers in seq3:", list(seq3))

    # 간격값이 음수면 range는 큰수 -> 작은수
    seq4 = range(10, 2, -1) # 10부터 3까지 거꾸로
    print("numbers in seq4:", list(seq4))

    # range를 이용하여 숫자 loop를 돌릴 수 있다
    for num in range(2,10,3):
        print(num)

def using_enumerate():
    """
    순차 자료형 loop시 객체와 함께 인덱스도 필요할 경우 enumerate로 묶음
    -> (인덱스, 객체) 튜플이 반환
    """
    colors = ["red", "yellow", "blue","green","orange"]

    # 해당 객체가 가진 index를 알 수 없음
    for color in colors:
        print("color:", color)

    # index는 enumerate를 통해서 튜플 언패킹을 해주면 됨
    for index, color in enumerate(colors):
        print("{}번 색상 -> {}".format(index+1, color))

    #
    nums = [3, 6, 1, 7, 4, 2, 9, 0]
    # 예: nums 리스트 내부 객체를 모두 두 배
    for index, num in enumerate(nums):
        # 내부 데이터에 접근
        nums[index] = num * 2

    print("RESULT:", nums)


def using_zip():
    """
    zip 객체
    - 여러 개의 순차형을 하나로 묶어서
    - 동일 위치의 요소들을 튜플로 묶음
    """
    english = "SUN", "MON", "TUE", "WED"
    korean = "일요일", "월요일", "화요일", "수요일", "목요일"
    # 길이가 다른 순차형 자료를 묶을 때는, 짧은 쪽이 기준이 된다
    engkor = zip(english, korean)
    print(engkor, type(engkor))     # 내부 데이터 확인 불가능

    # 기본 loop
    for pair in engkor:
        print(pair, type(pair))

    # zip은 1회 소비성 객체 -> 한번 루프를 돌면, 객체가 비어진다
    # 언패킹을 이용한 loop
    engkor = zip(english, korean)
    for eng, kor in engkor:
        print("영어 {} -> 한국어 {}".format(eng, kor))

    # 사전을 만들 때, zip 객체를 이용하기도 함.
    engkor = zip(english, korean)
    dct = dict(engkor)
    print("영한사전:", dct)


if __name__ == "__main__":
    # using_range()
    # using_enumerate()
    using_zip()