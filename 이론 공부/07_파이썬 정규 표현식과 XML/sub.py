import re

# sub를 통한 문자열 바꾸기
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))

#문자열 횟수 제어
print(p.sub('colour', 'blue socks and red shoes', count=1))

# subn - sub와 동일한 기능을 하지만 리턴되는 결과를 튜플로 리턴한다는 차이가 있다.
print(p.subn('colour', 'blue socks and red shoes'))

# sub 참조 구문 사용 (name - phone 구조를 phone, name 구조로 변경)
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)") # sub의 바꿀 문자열 부분에 \g<그룹명>을 이용하면 된다.
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
print(p.sub("\g<2> \g<1>", "park 010-1234-1234")) # 참조 번호 사용 가능

# sub 메서드의 입력 인수로 함수 넣기
def hexrepl(match):
    "Return the hex string for a decimal number" # 주석과 유사한 역할
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))