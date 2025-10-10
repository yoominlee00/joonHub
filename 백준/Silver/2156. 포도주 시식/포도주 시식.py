import sys

N = int(input())
wines = list(map(int,sys.stdin.read().split()))
#현재까지 최대 포도주양
if N == 1:
    print(wines[0])
    exit()

if N == 2:
    print(wines[0] + wines[1])
    exit()

dp = [0]*N

dp[0] = wines[0]
dp[1] = wines[0] + wines[1]
dp[2] = max(dp[1],dp[0]+wines[2],wines[1]+wines[2])


for i in range(3,N):
    dp[i] = max(dp[i-1],
                dp[i-2]+wines[i],
                dp[i-3]+wines[i-1]+wines[i])
print(dp[N-1])
    