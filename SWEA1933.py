# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
 
# [제약사항]
# N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
 
# [입력]
# 입력으로 정수 N 이 주어진다.

# [출력]
# 정수 N 의 모든 약수를 오름차순으로 출력한다.

n = int(input())
1 <= n <= 1000 

for x in range(1,n+1): # 범위를 0부터하면 ZeroDivisionError가 나옴. 1~n까지
    if n % x == 0:  #정수n을 x변수로 나눠서 나머지가 0이 된다면...
        print(x, end = ' ') # 한줄로 출력하기.
# 1 2 5 10 
# 정수10의 약수