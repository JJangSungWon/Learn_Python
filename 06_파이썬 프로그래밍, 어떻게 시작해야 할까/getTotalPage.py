def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1  # 소수점 아래 자리를 버리기 위해서 //사용


print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
