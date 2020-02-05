import re

# 긍정형 전방 탐색
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

# 부정형 전방 탐색
# .*[.](?!bat$).*$ - 확장자가 bat가 아닌 경우에만 통과
# .#[.](?!bat$|exe$).*$ - 확장자가 bat, exe가 아닌 경우에만 통과