#문자열
#주민등록번호 분리
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]

print(yyyymmdd)
print(num)

print('-'*50)
#주민등록번호에서 성별을 나타내는 자리 출력
pin = "881120-1068234"
print(pin[7])


print('-'*50)
#리스트
#리스트 순서 바꾸기
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

print('-'*50)
#리스트를 문자열로 만들기
a = ['Life', 'is', 'too', 'short']
#result = a[0] +' '+ a[1] +' '+ a[2] +' '+ a[3]
result = " ".join(a)
print(result)


