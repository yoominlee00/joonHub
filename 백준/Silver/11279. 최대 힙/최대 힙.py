import heapq
import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0 and lst:
        print(-heapq.heappop(lst))
    elif n == 0 and not lst:
        print(0)
    heapq.heappush(lst,-n)