# 25년 간의 수행 끝에 원재는 미래를 보는 능력을 갖게 되었다. 이 능력으로 원재는 사재기를 하려고 한다.
# 다만 당국의 감시가 심해 한 번에 많은 양을 사재기 할 수 없다.
# 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
#     1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
#     2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
#     3. 판매는 얼마든지 할 수 있다.
# 예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스 별로 첫 줄에는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고,
# 둘째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다.
# 각 날의 매매가는 10,000이하이다.


# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최대 이익을 출력한다.


# [예제 풀이]
# 1번째 케이스는 아무 것도 사지 않는 것이 최대 이익이다.
# 2번째 케이스는 1,2일에 각각 한 개씩 사서 세 번째 날에 두 개를 팔면 10의 이익을 얻을 수 있다.



import sys
sys.stdin = open("1859.txt", "r")

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    buy = list(map(int,input().split()))
    sale = buy[-1]
    
    cnt = 0
    for i in range(len(buy)-1,-1,-1): #범위는 뒤에서부터 -1씩만큼 본다.
        if sale > buy[i]: # 파는날가격이 사는 날가격보다 크면
            cnt += sale - buy[i] #파는가격에서 산사격을 빼서 더해라
        else: #가격이 같거나 사는날이 더 비쌀땐 안더함.
            sale = buy[i]
    print(f'#{tc} {cnt}')


#진숙님
T = int(input())

for i in range(1, T+1):

    N = int(input())
    price = list(map(int, input().split()))
    end = N-1
    max_ = max(price)
    start = sum_ = result = n = 0

    while start <= end:
        if price[0] == max_:
            result = 0
            break
        else:
            if price[start] < max_:
                sum_ += price[start]
                price[start] = 0
                start += 1
                n += 1
            elif price[start] == max_:
                result += ((price[start] * n) - sum_)
                price[start] = sum_ = n = 0
                start += 1
                max_ = max(price)
                if start == end:
                    break

    print(f'#{i} {result}')


#현식님
for test_case in range(1, int(input()) + 1):
    n = int(input())
    price = list(map(int, input().split()))

    mx = max(price)
    cnt = 0 # 최고가 아닌 날을 카운트
    hap = 0 # 최종답안
    if mx == price[0]:
        print(f"#{test_case} {0}")
    else:
        for i in range(n):
            if price[i] != mx: # 최고가가 아니라면
                hap -= price[i] # 이익이 마이너스
                cnt += 1 # 최고가 아니므로 카운트
            else:
                hap += cnt * mx # 최고가 라면 카운트 * 최고가
                if i != n - 1: # i값이 마지막이 아니라면
                    mx = max(price[i + 1:]) # 최고가를 찾기위해 현재 i이 아닌 i + 1 부터 리스트화한것에서 max값 찾기
                    cnt = 0 # 카운트 초기화
        print(f"#{test_case} {hap}")
                

#경욱님
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    
    # 이득
    profit = 0
    # 최대 가격
    max_price = 0
    # 최소 인덱스, 최대 인덱스
    min_index, max_index = 0, 0

    while True:
        # 0부터 시작해서, 끝까지 돌아봤을 때
        for i in range(min_index, N):
            # 만약 현재 저장된 최대 가격보다 더 큰 가격이 있으면
            if max_price < price[i]:
                # 그 값을 최대가격으로 설정하고
                max_price = price[i]
                # 최대 가격일 때의 인덱스르 저장
                max_index = i

        # 현재 저장된 최소 인덱스에서 최대 인덱스까지
        for j in range(min_index, max_index):
            # 최대 가격 - 해당하는 각 가격의 합이 이득으로 저장
            profit += (max_price - price[j])
        
        # 이득을 보고 나면 최대 가격 초기화
        max_price = 0
        # 최소 index를 실행한 곳 다음으로 이동
        min_index = max_index+1

        # N까지 전부 진행이 되면
        if min_index == N:
            # 출력 후
            print(f'#{test_case} {profit}')
            # while문 종료
            break               

#유영님
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    n_sell = list(map(int, input().split()))

    # 맨 끝에 값을 최대값으로 지정
    max_sell = n_sell[-1]
    cnt = 0

    # 맨 뒤에서 부터 0번째 인덱스까지 1씩 감소하면서 반복 순회 
    for i in range(n-2, -1, -1):
        # 현재 매매가가 최대값보다 크면 변경 
        if n_sell[i] >= max_sell:
            max_sell = n_sell[i]
        # 현재 매매가가 최대값보다 크지 않으면 차익을 cnt에 더함 
        else:
            cnt += max_sell - n_sell[i]

    print('#{} {}'.format(tc, cnt))  
