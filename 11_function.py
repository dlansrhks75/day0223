# 함수 : 어떤 문제해결을 위한 서로 관련있는 명령어 들의 집합

'''
def 함수이름(): #def는 function과 같은 기능을 합니다.
    명령어들
    :return [값1,값2,...]

파이썬의 함수는 여러 개의 값을 반환할 수 있습니다.
이것을 packing해서 tuple로 받을 수도 있고,
unpacking해서 변수에 할당할 수도 있습니다.
'''

# 두 개의 수를 매개변수로 전달받아 더하는 함수 만듥
# def add(a,b):
#     r= a+b
#     return r
#
# r = add(5,2)
# print(r)
# print(add(5,2))

#두 개의 수를 매개변수로 전달받아 더하기,뺴기,곱하기,나누기한 결과를 반환하는 함수를 만들어 봅시다.
def calc(a,b):
    add = a+b
    sub = a-b
    multi = a*b
    div = a//b
    return add,sub,multi,div

data = calc(5,2) # packing
a,b,c,d = calc(5,2) # unpacking
print(a,b,c,d)
