import sys
T = int(input())
for _ in range(T):
    N = int(input())
    N_lst = list(map(int,sys.stdin.readline().split()))
    M = int(input())
    dp = [0]*(M+1)
    dp[0] = 1
    for coin in N_lst:
        for i in range(coin,M+1):
            dp[i] += dp[i-coin]
    print(dp[M])
