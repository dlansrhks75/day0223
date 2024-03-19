a = [1,3,5,7,5,7,9]
b = {1,3,5,7,5,7,9}
print(a,type(a))
print(b,type(b))

a = set(a) #set으로 자료형을 변환 해줬기 때문에 이제는 중복된 값을 허용하지 않습니다.
print(a,type(a))