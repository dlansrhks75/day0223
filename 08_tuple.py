a = [1,3,5,7]
b = (1,3,5,7)

b = list(b)
print(type(b))
b.append(9)
print(b)

b = tuple(b)

print(type(b))