# module 전체를 import
import datetime  # datetime 모듈을 불러오기
from datetime import datetime as fdatetime  # datetime 모듈로부터 datetime 불러오기

def test_import():
    dt = datetime.datetime.now()
    print("dt:", dt)

def test_from_import():
    # datetime 모듈로부터 datetime 객체를 불러옴
    # 모듈명없이 객체명을 바로 부를 수 있음
    # datetime 객체를 import 할 때, 별칭을 붙였으므로 해당 별칭을 사용
    dt = fdatetime.now()
    print("from import as:", dt)

    # 객체 내장 변수 __module__을 확인하려면 해당 객체가
    # 어느 모듈에 속해있는지 확인 가능
    print("fdatetime이 속한 모듈:", fdatetime.__module__)

def sys_args():
    # sys 모듈 -> python 실행 환경 관련된 모듈
    import sys

    # sys.argv -> python에서 직접 실행시 command line으로부터 입력받은 인자의 목록
    # argv[0] -> 해당 모듈명
    # print(sys.argv)
    args = sys.argv[1:] # 실제 넘겨 받은 인수
    print("현재 모듈은 {}개의 인자를 전달 받음.".format(len(args)))
    for index, args in enumerate(args):
        print("{}번째 인자 => {}".format(index+1, args))


def random_ex():
    """
    랜덤 모듈 사용 예
    - 임의의 값을 선택해주는 기능
    """
    import random

    # 경우에 따라서는 난수 발생을 위한 seed 값을 고정시켜서
    # 재현성을 확보해야 할 경우가 있다
    # 임의로 seed를 고정시켜야 함
    # random.seed(42)     # 같은 결과값. 개발할 때 재현성 확인에 용이.

    # print("임의의 난수:", random.random())   # 0부터 1사이의 실수 난수
    print("임의의 정수 난수:", random.randint(1, 6))   # 1부터 6사이의 정수 난수
    print("범위 지정 난수 1:", random.randrange(101))  # 0부터 100 사이의 범위 난수
    print("범위 지정 난수 2:", random.randrange(1, 101, 3))   # 1부터 100(간격 3)

    # 단순 난수 발생 이외에 여러가지 임의 선택 기능을 제공
    seqvar = ["짬뽕", "짜장", "짬짜면"]
    print("원본 리스트", seqvar)
    # shuffle
    random.shuffle(seqvar)
    print("섞은 리스트", seqvar)

    # 선택: choice
    menu = random.choice(seqvar)
    print("선택된 메뉴:", menu)

    # 샘플링: 모집단으로부터 임의의 데이터를 추출할 때
    sample = random.sample(range(1, 101), 10)   # 1~ 100 범위 중 10개를 샘플링
    print("sampling:", sample)





# 모듈의 __name__ : 해당 모듈의 이름
# 1. 최상위 모듈로 실행되었을 때 -> __main__
# 2. import 되었을 때 -> 해당 모듈의 파일명
print("현재 모듈의 __name__:", __name__)
if __name__ =="__main__":
    print("현재 모듈은 최상위 모듈로 실행되고 있습니다.")
    # test_import()
    # test_from_import()
    # sys_args()
    random_ex()

else:
    print("현재 모듈은 다른 모듈로부터 import 되었습니다.")