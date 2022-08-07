t = int(input())

for tc in range(1,t+1):
    n = int(input())
    buy = list(map(int,input().split()))
    for i in range(1,n+1):
        a = buy[0]
        b = buy[1]
        c = buy[2]
        sale =  (c-a) + (c-b)
        if a and b  > c:
            ans = 0
        else :
            ans = sale
    print(f'#{tc} {ans}')            
    
    ###백만장자문제 뭔소린지,,모르겠음,,,
    ##다른거 풀고와서 다시 도전해본다...