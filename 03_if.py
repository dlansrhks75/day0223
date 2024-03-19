#if 조건식:
#     명령어1
#     명령어2
#     ..
# else:
#     명령어3
#     명령어4
#     ..

# 연습) 어떤 수를 입력받아서 짝수인지 홀수인지 판별하여 출력해 봅니다.
# n = int(input("숫자를 입력하시오==>"))
# re = n%2 ==0
# if(re):
#     print("짝수")
# else:
#     print("홀수")

# 연습) 사용자한테 3개의 수를 입력받아 그 중에 가장 큰 수를 찾아서 출력하시오.
# a = int(input("첫번쨰 숫자를 입력하시오==>"))
# b = int(input("두번쨰 숫자를 입력하시오==>"))
# c = int(input("세번쨰 숫자를 입력하시오==>"))
# if a>b:
#     if a>c:
#         max = a
#     else:
#         max = c
# else:
#     if b>c:
#         max = b
#     else:
#         max=c
# print("가장 큰 수는 : ",max)

# if 조건1:
#     명령1
# elif 조건2:
#     명령2
# elif 조건3
#     ...
# else:
#     ..

# 연습) 0~9 사이의 정수를 입력받아 한글표기식 출력하는 코드를 작성해 봅니다.
# n = int(input("0~9 사이의 정수를 입력하시오==>"))
# if n==0:
#     print("영")
# elif n==1:
#     print("일")
# elif n==2:
#     print("이")
# elif n==3:
#     print("삼")
# elif n==4:
#     print("사")
# elif n==5:
#     print("오")
# elif n==6:
#     print("육")
# elif n==7:
#     print("칠")
# elif n==8:
#     print("팔")
# elif n==9:
#     print("구")
# else:
#     print("올바르지 않은 값 입력")

# 연습) 0~9 사이의 정수를 입력받아 한글표기식 출력하는 코드를 작성해 봅니다.
n = int(input("0~9 사이의 정수를 입력하시오==>"))
if n>=0 and n<=9:
    if n == 0: kor = "영" # 수행해야 할 작업이 1개이면, 한 줄로 작업할 수 있습니다.
    elif n == 1: kor = "일"
    elif n == 2: kor = "이"
    elif n == 3: kor = "삼"
    elif n == 4: kor = "사"
    elif n == 5: kor = "오"
    elif n == 6: kor = "육"
    elif n == 7: kor = "칠"
    elif n == 8: kor = "팔"
    elif n == 9: kor = "구"
    print(kor)
else:
    print("입력범위를 넘었어요.")