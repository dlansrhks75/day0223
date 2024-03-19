a = {"홍길동",20,"서울시 마포구 서교동"}
b = {
    "name":"홍길동",
    "age":20,
    "addr":"서울시 마포구 서교동",
}

for row in b.items(): #패킹
    key,value = row   #언패킹
    print(key,value)

# print(a,type(a))
# print(b,type(b))
#
# print(b['name'])
# print(b['age'])
# print(b['addr'])

# data = 5,7
# print(data)