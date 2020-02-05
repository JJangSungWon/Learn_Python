import re

# DOTALL, S - 줄바꿈 포함
p = re.compile('a.b')  # .의 경우 줄바꿈 문자를 제외한 모든 문자를 의미한다.
m = p.match('a\nb')
print(m)  # 따라서 None이 출력된다.

p = re.compile('a.b', re.DOTALL)  # re.DOTALL 옵션을 통해 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.(=re.S)
m = p.match('a\nb')
print(m)

# IGNORECASE, I - 대소문자 구분 없이 매치
p = re.compile('[a-z]')
m = p.match('AB')
print(m)

p = re.compile('[a-z]', re.I)
m = p.match('AB')
print(m)

# MULTILINE, M - ^, &문자와 연관(문자열의 처음과 마지막), 문자열의 각 라인마다 ^와 $를 적용해 주는 것이다.
p = re.compile("^python\s\w+")
data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))  # 문장 전체의 처음만 인식(각 라인의 처음으로 인식하지 못하는 상황)

p = re.compile("^python\s\w+", re.MULTILINE)  # 각 라인의 처음으로 인식
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))

# VERBOSE, X - 정규식을 주석 또는 라인 단위로 구분
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')  # 쉽게 이해하기 힘든 형태

charref = re.compile(r"""
&[#]                # Start of a numeric entity reference
(
    0[0-7]+         # Octal form
  | [0-9]+          # Decimal form
  | x[0-9a-fA-F]+   # Hexadecimal form
)
;
""", re.VERBOSE)  # re.X를 통해 조금 더 쉬운 형태로 바꿀 수 있습니다.
