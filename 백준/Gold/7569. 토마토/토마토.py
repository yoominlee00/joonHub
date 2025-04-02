import sys
from collections import deque
M, N ,H = map(int,sys.stdin.readline().split())
graph = []
for _ in range(H):
    lst = []
    for _ in range(N):
        lst.append(list(map(int,sys.stdin.readline().split())))
    graph.append(lst)



dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]
q = deque()

for i in range(N):
    for j in range(M):
        for k in range(H):
            if graph[k][i][j] == 1:
                # 가중치 대신 날짜를 넣는다
                q.append((k,i,j,0))
max_day =0

while q:
    z,x,y,day = q.popleft()
    max_day = max(max_day,day)
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nz<H and 0<=nx<N and 0<=ny<M:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = 1
                q.append((nz,nx,ny,day+1))


for i in range(N):
    for j in range(M):
        for k in range(H):
            if graph[k][i][j] == 0:
                print(-1)
                sys.exit()
print(max_day)