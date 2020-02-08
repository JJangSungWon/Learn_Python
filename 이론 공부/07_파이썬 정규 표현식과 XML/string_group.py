import re

# 그룹핑된 문자열에 이름 붙이기 (\w+) -> (?P<name>\w+)
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

# 그룹명을 이용한 재참조
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
p.search('Paris in the the spring').group()