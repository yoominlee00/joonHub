import sys
import heapq
N, M, K, X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
distance = [float('inf') for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

def dikstra(start):
    q = [(0,start)]
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for neighbor in graph[now]:
            if distance[neighbor] > dist + 1 :
                heapq.heappush(q,(dist+1,neighbor))
                distance[neighbor] = dist+1
dikstra(X)
ck = False
for i,val in enumerate(distance):
    if val == K:
        ck = True
        print(i)

if ck == False:
    print(-1)
