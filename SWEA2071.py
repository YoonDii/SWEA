#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
#(소수점 첫째 자리에서 반올림한 정수를 출력한다.)


import sys
sys.stdin = open("2071.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for x in range(1, T + 1):
    num = list(map(int,input().split()))
    a = sum(num)/len(num) #총합에서 길이만큼나누기(요소개수)
    a = round(a) #반올림함수 round()
    print("#{} {}".format(x,a))
#1 24
#2 29
#3 27