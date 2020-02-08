#tuple
a = (1, 2, 3)
a = a + (4,)
print(a)

print('-'*50)
#dictionary
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

print('-'*50)
#set
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a) # 중복을 허용하지 않는 set의 특징 이용
b = list(aSet)
print(b)

print('-'*50)
#변수
a = b = [1, 2, 3] #a, b는 동일한 객체를 가르킨다.
a[1] = 4
print(b) #b에도 영향이 간다.







