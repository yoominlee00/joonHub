import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()
visited = [False]*(N+1)
v = [False]*(N+1)
result1 = []
result2 = []

def dfs(node):
    visited[node] = True
    result1.append(node)
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

def bfs(node):
    q = deque([node])
    v[node] = True
    while q:
        cur = q.popleft()
        result2.append(cur)
        for i in graph[cur]:
            if not v[i]:
                v[i] = True
                q.append(i)


dfs(V)
bfs(V)
print(' '.join(map(str,result1)))
print(' '.join(map(str,result2)))
