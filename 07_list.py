# a = [1,3,5,7]
# print(a)
# print(type(a))
#
# print(a[0])
# print(a[1])
#
# print(len(a))
#
# for i in range(len(a)):
#     print(a[i],end=" ")
# print()
# for i in a:
#     print(i, end=" ")

a = [1,3,5,7]
# 연습) 리스트의 요소를 거꾸로 출력해봅니다.
for i in range(len(a)-1,-1,-1): #-1까지로 설정했기 때문에 for문의 특성상 -1을 제외하고 0번째까지 반복해서 인덱스번호가 0번째인 것까지 반복합니다.
    print(a[i],end=" ")
print()

for i in reversed(a):
    print(i, end=" ")

