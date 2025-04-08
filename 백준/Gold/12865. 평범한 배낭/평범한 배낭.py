import sys
N, K = map(int,sys.stdin.readline().split())
A = []
B = []
dp = [[0]*(K+1) for _ in range(N+1)]
for _ in range(N):
    a, b = map(int,sys.stdin.readline().split())
    A.append(a)
    B.append(b)

for i in range(1,N+1):
    for w in range(K+1):
        dp[i][w] = dp[i-1][w]
        if A[i-1] <= w:
            dp[i][w] = max(dp[i-1][w-A[i-1]]+B[i-1],dp[i][w])
print(dp[N][K])