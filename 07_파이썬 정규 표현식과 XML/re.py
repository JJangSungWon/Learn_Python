import re

p = re.compile("정규 표현식")

# match
m = p.match("조사할 문자열")
if m:
    print('Match found: ', m.group())
else:
    print('No match')

# search (처음부터 조사하지 않는 것이, match와 차이점)
m = p.search("조사할 문자열")

# findall (문자열중 정규 표현식에 매치되는 것들을 모아 리스트로 리턴한다)
m = p.findall("조사할 문자열")

# finditer (findall과 동일하지만 그 결과로 반복 가능한 객체를 리턴한다는 차이점이 있다)
m = p.finditer("조사할 문자열")
