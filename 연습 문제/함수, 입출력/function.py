#입력을 정수 n으로 받았을 때, n 이하까지의 피보나치(fibonacci) 수열을 출력하는 함수

def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))