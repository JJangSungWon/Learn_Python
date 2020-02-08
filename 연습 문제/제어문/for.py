#학급의 평균 점수를 구하기

#for문
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

print("*"*50)

#for문을 이용하지 않을때
total = sum(A)
len = len(A)
average = total / len
print(average)