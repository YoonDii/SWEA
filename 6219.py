# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오

# (단, 약수가 2개일 경우 소수임을 나타내십시오)


n = int(input())

cnt = 0
for i in range(1,n+1):
    if n % i == 0 :
        print(f'{i}(은)는 {n}의 약수입니다.')
        cnt += 1
    if cnt == 2:
        print(f'{n}(은)는 1과 {n}로만 나눌 수 있는 소수입니다.')