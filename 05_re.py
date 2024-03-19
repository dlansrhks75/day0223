import re

db = '''
3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1234  Tiger 555
1548  Kerry 534
'''
# print(db)

# 연습) 숫자만 출력하기
# result = re.findall("[0-9]+",db)
# print(result)
# print(type(result))

# 연습) 이름만 출력하기
# result = re.findall("[A-Za-z]+",db)
# print(result)

# 연습) 전화번호만 출력하기
# phones = re.findall("[0-9]{4}",db)
# phones = re.findall("\\d{4}",db)
# phones = re.findall("^\\d+",db, re.MULTILINE)
# print(phones)

# 연습) 아이디만 추출하여 출력하기
# ids = re.findall("\d+$",db,re.MULTILINE)
# print(ids)

# 연습) T로 시작하는 이름만 찾아서 출력
# startT = re.findall("T[a-z]+",db)
# print(startT)

# 연습) T로 시작하지 않는 사람의 이름만 찾아서 출력
#notT = re.findall("[^T][a-z]+",db) #왼쪽과 같이 하면 모든 이름을 불러오면서 이름의 첫번째 문자가 T인 경우 T를 제외하고 나머지 이름을 불러옵니다.
# notT = re.findall("[A-SU-Z][a-z]+",db)
# print(notT)

