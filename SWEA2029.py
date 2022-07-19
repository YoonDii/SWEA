# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라

import sys
sys.stdin = open("2029.txt", "r")

T = int(input())
for x in range(1, T + 1): # x == 1~T까지
    a, b = map(int, input().split()) # map은 list의 요소를 지정된 함수도 변환해줌.
    print("#{} {} {}".format(x, a//b,a%b)) #str.format()로 문자열변환 추출.
#1 4 1
#2 2 3
#3 24 9