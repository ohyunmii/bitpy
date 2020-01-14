# class
# class는 member(data), method(func) 한 namespace안에 작성한 것
# class는 새로운 데이터 자료형의 설계도
# class를 실제 객체로 만드는 작업을 instance화라고 함.
#   만들어진 실객체는 인스턴스라고 한다

# class의 정의
class MyString(str):
    pass
    # 부모 클래스로부터 str을 확장하여 만듬
    # MyString은 str로부터 모든 멤버와 메서드를 상속받음

print("--- MyString ")
s = MyString("새로 만든 MyString class")
print("MyString:", s)
s = MyString("Python Object Oriented Programming")
print("MyString:", s)
# MyString은 str을 확장하여 만들었기 때문에, str이 가진 모든 기능을 사용할 수 있음
print("s.lower:", s.lower())

# type 확인
print("s is", type(s))
print("s class:", s.__class__) # 어떤 클래스?

# 부모 클래스 확인
print("s의 부모는?", MyString.__bases__)   # 부모 클래스 확인
print("s는 MyString의 instance?", isinstance(s, MyString))
print("s는 str의 instance?", isinstance(s, str))



