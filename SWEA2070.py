#2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.


import sys
sys.stdin = open("2070.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for x in range(1, T+1):
    a, b = map(int,input().split())
    if a < b :
        print("#{} {}".format(x, '<'))
    elif a == b:
        print("#{} {}".format(x, '='))
    else :
        print("#{} {}".format(x, '>'))

#1 <
#2 =
#3 >