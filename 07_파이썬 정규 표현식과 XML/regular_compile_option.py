import re

# DOTALL, S - 줄 바꿈 문자 포함 여부 관련
p = re.compile('a.b')
m = p.match('a\nb')
print(m)  # .은 \n을 포함하지 않는다는 사실을 알 수 있다.

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)  # re.DOTALL 컴파일 옵션을 통해서 \n을 포함하는 형태로 바뀌었다.

# IGNORECASE, I - 대,소문자 구분 관련
p = re.compile('[a-z]')
print(p.match('PYTHON'))  # 대문자 경우 인식하지 못한다.

p = re.compile('[a-z]', re.I)
print(p.match('PYTHON'))  # 대문자도 인식한다.

# MULTILINE, M - ^(문자열의 처음), $(마지막)와 연관된 옵션
p = re.compile("^python\s\w+")
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))  # python이라는 문자열이 사용된 첫 번째 라인만 매치된 결과

p = re.compile("^python\s\w+", re.MULTILINE)
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data)) # 각 라인의 처음 조사

# VERBOSE, X - 정규식을 주석 또는 라인 단위로 구분할 수 있도록 한다.
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);') # 쉽게 알아보기 힘든 형태, 맨 앞의 r은 Raw String임을 알려준다.

charref = re.compile(r"""
 &[#]               # Start of a numeric entity reference
 (
    0[0-7]+         # Octal form
  | [0-9]+          # Decimal form
  | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                  # Trailing semicolon
 """, re.VERBOSE)