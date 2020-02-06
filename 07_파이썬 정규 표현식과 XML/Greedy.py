import re

s = '<html><head.<title>Title</title>'
print(len(s))

# Greedy
print(re.match('<.*>', s).span())  # *는 매치할 수 있는 최대한의 문자열을 소모시켜 버린다.
print(re.match('<.*>', s).group())

# Non-Greedy
print(re.match('<.*?>', s).group())  # ?를 통해 탐욕을 제한할 수 있다.(가장 최소한의 반복을 수행하도록 도와준다)
