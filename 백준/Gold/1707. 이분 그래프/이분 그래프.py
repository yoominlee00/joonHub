import sys
sys.setrecursionlimit(10**6)
K = int(input())


def dfs(node):
    global ch
    visited[node] = True
    if check[node] == None:
        check[node] = 0
    
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            if check[node] == 0:
                check[i] = 1
            else:
                check[i] = 0
            dfs(i)
        else:
            if (check[i] == 0 and check[node] == 0) or (check[i] == 1 and check[node] == 1):
                ch = False
                return 
            
for _ in range(K):
    V, E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [False]*(V+1)
    check = [None]*(V+1)
    ch = True
    for _ in range(E):
        a, b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    # 연결되지 않은 부분도 돌리기
    for i in range(1, V + 1):
        if not visited[i] and ch:
            dfs(i)

    if ch == True:
        print('YES')
    else:
        print('NO')


