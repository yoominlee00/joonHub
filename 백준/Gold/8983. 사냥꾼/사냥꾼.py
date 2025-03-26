import sys
import heapq

M, N, L = map(int,sys.stdin.readline().split())
hunt = list(map(int,sys.stdin.readline().split()))
heapq.heapify(hunt)
animal = []
result = []
cnt = 0

for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    heapq.heappush(animal,(x+y,x-y))
cnt = 0

for i in hunt:
    while animal and animal[0][0] <= i + L:
        heapq.heappush(result,animal[0][1])
        heapq.heappop(animal)
    while result and result[0] > L - i:
        heapq.heappop(result)
    cnt = max(cnt,len(result))

print(cnt)



