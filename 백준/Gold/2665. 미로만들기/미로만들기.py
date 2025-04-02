import sys, heapq
N = int(input())
graph = []
distance = [[float('inf')]*N for _ in range(N)]
for _ in range(N):
    lst = list(map(int,sys.stdin.readline().strip()))
    graph.append(lst)

# 값 두개로?
def dikstra(a,b):
    q = [(0,(a,b))]
    distance[a][b] = 0
    dx = [ 1, -1, 0, 0]
    dy = [ 0, 0, 1, -1]
    while q:
        dist, now = heapq.heappop(q)
        a = now[0]
        b = now[1]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<= x < N and 0 <= y <N:
                w = 1- graph[x][y]
                new_cost = distance[a][b] + w
                if new_cost  < distance[x][y]:
                    q.append((new_cost,(x,y)))
                    distance[x][y] = new_cost
    return distance[N-1][N-1]
        
print(dikstra(0,0))


