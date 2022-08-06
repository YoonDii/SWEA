t = int(input())

for tc in range(1,t+1):
    n, k = map(int,input().split())
    puzzle = [list(map(int,input().split()))for i in range(n)]
    cnt = 0
    total = 0
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == n-1:
                if cnt == k:
                    total +=1
                cnt = 0
        for j in range(n): 
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == n-1:
                if cnt == k:
                    total += 1
                cnt = 0

    print(f'#{tc} {total}')