import sys
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def dfs(node):
    global cnt
    cnt += 1
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(1)
print(cnt-1)
