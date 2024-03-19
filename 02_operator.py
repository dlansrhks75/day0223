# 연산자 : 산술, 비교, 논리
# 산술 : + - * /(실수 나누기) //(정수 나누기) **(지수승) %(나머지)
# 논리 : and or not

# a,b = 5,2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b)
# print("-"*50) #"-"를 50개 출력
# a+=1;
# print(a)

# print(a>b)
# print(a>=b)
# print(a<b)
# print(a<=b)
# print(a==b)
# print(a!=b)

# a = "10"
# b = "20"
# print(a+b)
# print(int(a)+int(b))

# a=10
# b=-5
# c=0
# d="hello"
# e=32.7
# f=0.0
# print(a,bool(a))
# print(b,bool(b))
# print(c,bool(c))
# print(d,bool(d))
# print(e,bool(e))
# print(f,bool(f))

# print(int(True))
# print(int(False))

# name=input("이름을 입력하시오==>")
# print(name)

# 연습) 사용자한테 어떤 숫자 하나를 입력받아 +1을 하여 출력해봅니다.
# n=input("숫자를 입력하시오==>")
# print(int(n)+1)

# 연습) 사용자한테 나이를 입력받아 20이상인지 판별하여 True,False를 출력해 봅니다.
# age=input("나이를 입력하시오==>")
# re = int(age)>=20
# print(re)

#연습) 두 사람의 나이를 입력받아 모두 20살 이상이면 True, 그렇지 않으면 False를 출력해 봅니다.
age1 = int(input("첫번째 나이를 입력하시오==>"))
age2 = int(input("두번째 나이를 입력하시오==>"))
re = age1>=20 and age2>=20
print(re)