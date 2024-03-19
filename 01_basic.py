# 처음 실행 : ctrl + shift + f10
# 수정 후 실행 : shift + f10
# print('hello')
# print('python')
# print(100)

# 연습) hello를 화면에 3번 출력하시오.
# print('hello')
# print('hello')
# print('hello')
# print('hello\nhello\nhello')
# print('hello\n'*3)

# 프로그램 : 코드(함수), 데이터(변수)
# a=3
# print(a);

# 데이터 : 변수(a), 상수(3)
# 데이터 : 숫자(정수,실수), 문자로 구성
# a=3
# b="hello"
# print(a)
# print(b)
# print("korea")

# int(정수) float(실수) str(문자열) bool(논리형)
# a=20
# b=56.7
# c="hello"
# d=True
# print(a)
# print(b)
# print(c)
# print(d)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# a=3
# b=4
# print("a:",a)
# print("b:",b)

# a,b의 값을 서로 맞바꾸어 출력해 봅니다.
# c=a
# a=b
# b=c
# print("a:",a)
# print("b:",b)

# 파이썬에서는 위처럼 임시변수를 생성해서 값을 맞바꿔줄 필요없이 다중대입이 가능합니다.
# 이러한 개념으로 인해 파이썬의 함수는 여러 개의 값을 반환할 수 있습니다.
a,b = 3,4
print(a)
print(b)
a,b = b,a
print(a)
print(b)
