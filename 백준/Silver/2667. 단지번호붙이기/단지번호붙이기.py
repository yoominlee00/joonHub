import sys
from collections import deque
N = int(input())
graph = []
lst = []

for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().strip())))
visited = [[False]*N for _ in range(N)]

def check(x,y):
    cnt = 0
    q = deque()
    q.append((x,y))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while q:
        x, y= q.popleft()
        visited[x][y] = True
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return cnt

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            visited[i][j] = True
            lst.append(check(i,j))
lst.sort()
print(len(lst))
for i in lst:
    print(i)
