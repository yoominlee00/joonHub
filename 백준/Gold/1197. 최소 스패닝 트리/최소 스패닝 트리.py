import sys
import heapq
V, E = map(int, sys.stdin.readline().split())
graph = [[] for i in range(V+1)]
visited = [False]*(V+1)

for _ in range(E):
    a, b, w = map(int,sys.stdin.readline().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
#가중치로 힙
heap =[(0,1)]
visited[0] = True
weight = 0
while heap:
    w, now = heapq.heappop(heap)
    if visited[now]:
        continue
    visited[now] = True
    for neighbor, cost in graph[now]:
        if not visited[neighbor]:
            heapq.heappush(heap,(cost,neighbor))
    weight += w
print(weight)