import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(N+1)]
visited = [False]*(N+1)
q = deque()
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        visited[i] = True
        q.append(i)
        cnt += 1
        while q:
            cur = q.popleft()
            for neighbor in graph[cur]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True
print(cnt)
