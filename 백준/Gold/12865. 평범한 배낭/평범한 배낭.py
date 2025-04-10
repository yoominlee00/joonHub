import sys
N, K = map(int,sys.stdin.readline().split())
item = []
for _ in range(N):
    m, v = map(int,sys.stdin.readline().split())
    item.append((m,v))
dp = [0]*(K+1)
for m,v in item:
    for w in range(K,m-1,-1):
        dp[w] = max(dp[w-m] + v,dp[w])
print(dp[K])