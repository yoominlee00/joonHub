import heapq
import sys

N = int(input())
lst = list(map(int,sys.stdin.read().splitlines()))
heapq.heapify(lst)
total = 0
while len(lst) > 1:
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    heapq.heappush(lst,a+b)
    total += a+b
print(total)