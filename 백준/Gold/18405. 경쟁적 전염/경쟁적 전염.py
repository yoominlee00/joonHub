import sys
import heapq
N,K = map(int,sys.stdin.readline().split())
graph = []
q = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
S,X,Y = map(int,sys.stdin.readline().split())

for i in range(N):
    for j in range(N):
        num = graph[i][j]
        if num != 0:
            heapq.heappush(q,(0,num,i,j))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while q:
    day, num, x, y =heapq.heappop(q)
    if day >= S:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = num
                heapq.heappush(q,(day+1,num,nx,ny))

print(graph[X-1][Y-1])