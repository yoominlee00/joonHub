import sys
N = int(input())
lst = list(map(int,sys.stdin.readline().split()))
# i 번째 수를 마지막으로 하는 LIS 길이 (자기자신 하나 기본값으로 저장)
dp = [1]*N

#순차탐색
for i in range(N):
    #탐색한 범위까지 또 비교
    for j in range(i):
        # 자기보다 작은 게 있으면 그때까지 누적한 값 + 자기자신인 1
        # 그 중 가장 긴 수열 채택 ! 
        if lst[j] < lst[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))