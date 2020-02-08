#0~9까지의 숫자가 각각 한 번씩만 사용된 것인지 확인하는 함수 작성

def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

print(chkDupNum("0123456789")) #True
print(chkDupNum("012345678"))  #False
    
    

