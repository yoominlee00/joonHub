import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().strip()))
visited = [[False]*M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            q = deque()
            q.append((i,j))
            cnt +=1
            while q:
                x,y = q.popleft()
                visited[x][y] = True
                if graph[x][y] == '-':
                    if y+1 < M:
                        if graph[x][y+1] == '-':
                            q.append((x,y+1))
                elif graph[x][y] == '|':
                    if x+1 < N:
                        if graph[x+1][y] == '|':
                            q.append((x+1,y))
print(cnt)

