import sys 
N = int(input())
game = []
for _ in range(N):
    game.append(list(map(int,sys.stdin.readline().split())))
dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][1] = 1

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == 1 and j ==1:
            continue
        if j > 1:
            for j_x in range(1,j):
                if (j - j_x) == game[i-1][j_x-1]:
                    dp[i][j] += dp[i][j_x]
        if i > 1:
            for j_y in range(1,i):
                if(i - j_y) == game[j_y-1][j-1]:
                    dp[i][j] += dp[j_y][j]
print(dp[N][N])