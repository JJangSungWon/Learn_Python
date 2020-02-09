import re

s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

#전화번호 패턴(뒤의 숫자 4개를 *로 바꾸기 위에 앞부분 그룹핑한다)
pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)
