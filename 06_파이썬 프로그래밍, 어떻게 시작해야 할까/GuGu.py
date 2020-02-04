def GuGu(n):
    #print(n) #입력값 확인
    result = []

    i =  1
    while i <= 9:
        result.append(n * i)
        i = i + 1
    return result

result = GuGu(2)
print(result)
