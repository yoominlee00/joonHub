import sys
input = sys.stdin.readline

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[10**9] * (N) for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
#크기
for l in range(1, N):
    #시작 지점 -> 크기에 맞춘다.
    for i in range(N - l): 
        # 최소를 찾는 것 ! 이므로 무한대로 초기화
        j = i + l
        for m in range(i,j):
            cost = dp[i][m] + dp[m+1][j] +lst[i][0] * lst[m][1]* lst[j][1]
            dp[i][j] = min(dp[i][j],cost)
print(dp[0][N-1])