def solution(info, n, m):
    L = len(info)
    dp = [[[False]*m for _ in range(n) ] for _ in range(L)]

    if info[0][0] < n: 
        dp[0][info[0][0]][0] = True
    if info[0][1] < m:
        dp[0][0][info[0][1]] = True
    
    for i in range(1,L):   
        a_cost, b_cost = info[i] 
        for j,j_val in enumerate(dp[i-1]):
            for k,k_val in enumerate(j_val):
                if k_val:
                    if (j + a_cost) < n:
                        dp[i][j + a_cost][k] = True
                    if (k + b_cost) < m:
                        dp[i][j][k + b_cost] = True
    min_a = float('inf')
    for i in range(n):
        for j in range(m):
            if dp[L-1][i][j]:
                min_a = min(min_a,i)
    if min_a != float('inf'):
        answer = min_a
    else:
        answer = -1
    return answer