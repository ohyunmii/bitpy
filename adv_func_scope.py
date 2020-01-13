# 함수의 영역 rules
x = 1

def scope_func(a):
    print("LOCAL:", locals())
    print("x in locals?", "x" in locals())
    print("x in globals?", "x" in globals())
    return a + x        # x는 local scope에 없기 때문에 global x를 사용

print(scope_func(10))


def scope_func2(a):
    x = 2       # x의 할당 작업이 일어났으므로 local scope에 x가 생길 것.
    print("x in locals?", "x" in locals())
    return a + x
    # 함수의 내부에서 x의 할당 작업이 일어났으므로 local scope에 x가 생성

print(scope_func2(10))


def scope_func3(a):
    global x        # 지금부터 x는 글로벌 변수임을 명시
    x = 3
    print("x in locals?", "x" in locals())
    print("x in globals?", "x" in globals())
    return a + x

print("scope func3:", scope_func3(10))
# scope_func3 내부에서 global x를 변경
print("global x:", x)

# namespace 확인
# locals 함수 -> local scope의 namespace 확인
# globals 함수 -> global scope의 namespace 확인
# dir 함수 -> global scope 혹은 built-in scope의 namespace 확인
print("DIR:", dir())    # global scope의 namespace 확인
print("Built-in scope:", dir('__builtins__')) # built-in scope namespace 확인

