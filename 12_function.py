# 연습) 함수만들기 : 두 개의 수를 매개변수로 전달받아 그 중에 큰 수를 찾아 반환하는 함수를 만들고 호출하기.
def max(a,b):
    if(b>a):
        a = b
    return a

# 연습) 3개의 수를 매개변수로 전달받아 그 중에 큰 수를 찾아 반환하는 함수를 정의하고 호출하기. 이때 두 수중에 큰 수를 찾는 함수를 활용합니다.
def max3(a,b,c):
    return max(max(a,b),c)
print(max3(5,1,12))
