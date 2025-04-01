import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
graph = []
new_graph = []
visited = []
q = deque()
for _ in range(N):
    lst = list(map(int,sys.stdin.readline().split()))
    graph.append(lst)
q = deque()

def check(a,b,visited,rem):
    q.append((a,b))
    visited[a][b] = True
    while q:
        a, b = q.popleft()
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        cnt = 0
        for i in range(4):
            new_a = a + dx[i]
            new_b = b + dy[i]
            if 0 <= new_a < N and 0 <= new_b < M and not visited[new_a][new_b]:
                curr = graph[new_a][new_b]
                if curr == 0:
                    cnt += 1
                elif not visited[new_a][new_b] and curr > 0:
                    visited[new_a][new_b] = True
                    q.append((new_a,new_b))
        rem[a][b] += cnt
area = 0

def ice(n):
    rem = [[0]*M for _ in range(N)]
    area = 0
    visited = []
    for _ in range(N):
        visited.append([False]*M)

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                if not visited[i][j]:
                    area +=1
                    check(i,j,visited,rem)
    ##
    if area == 0:
        return 0
    if area >= 2:
        return n
    
    for i in range(N):
        for j in range(M):
            graph[i][j] -= rem[i][j] 
            if graph[i][j] < 0 :
                graph[i][j] = 0
    return ice(n+1)

print(ice(0))
