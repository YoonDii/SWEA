#주어진 숫자부터 0까지 순서대로 찍어보세요

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for x in range(T,-1,-1): #range(A, B, C) A부터 C 숫자만큼의 간격으로 B-1 까지의 정수 범위를 반환합니다. 
	print(x,end =' ') #공백제거해서 한줄로 나오게 하기
#8 7 6 5 4 3 2 1 0