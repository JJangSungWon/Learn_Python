import re

p = re.compile('[a-z]+')

# match
m = p.match("python") #위 두 줄을 m = re.match('[a-z]+', "python")으로 작성할 수도 있다.
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# search
n = p.search("3 python")
print(n.group())
print(n.start())
print(n.end())
print(n.span())