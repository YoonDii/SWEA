# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

# 주어질 숫자는 30을 넘지 않는다.


n = int(input())
n < 30
for x in range(0,n+1): # 0~n까지
    x = 2**x    # x는 2의제곱으로 나와야한다.
    print(x, end = ' ') # 한줄로 출력하기
    
    # 1 2 4 8 16 32 64 128 256