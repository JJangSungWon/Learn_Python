result = 0
for n in range(1, 1000):  # 1 ~ 999 범위
    if n % 3 == 0 or n % 5 == 0:  # 15와 같이 3과, 5로 둘 다 나뉘어지는 수를  중복으로 더하지 않기 위해 or 사용
        result += n
print(result)
