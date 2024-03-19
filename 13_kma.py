import re
import requests

url ="https://devweather.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

text = requests.get(url).text
# print(text)

# 위 text의 내용 중에서 <title>태그 안에 문자열 불러오기.
# title = re.findall("<title>(.+)</title>",text)
# print(title)
#
# for row in title:
#     print(row)

# list = re.findall('<location wl_ver="3">(.+)</location>',text,re.DOTALL)
# print(len(list))
list = re.findall('<location wl_ver="3">(.+?)</location>',text,re.DOTALL)
print(len(list),type(list))

# 연습) 모든 도시명을 추출하여 추출하기
for row in list:
    city = re.findall("<city>(.+)</city>",row)
    data = re.findall("<data>(.+?)</data>",row,re.DOTALL)
    for d in data:
        tmEf = re.findall("<tmEf>(.+)</tmEf>",d)
        wf = re.findall("<wf>(.+)</wf>",d)
        tmn = re.findall("<tmn>(.+)</tmn>",d)
        tmx = re.findall("<tmx>(.+)</tmx>",d)
        print(city[0],tmEf[0],wf[0],tmn[0],tmx[0])