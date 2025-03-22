import sys
import heapq

N = int(sys.stdin.readline())
min_h = []
max_h = []
for i in range(N):
    n = int(sys.stdin.readline())
    if not min_h:
        heapq.heappush(min_h,n)
        heapq.heappush(max_h,-n)
    else:
        if i%2 == 0:
            if min_h[0] < n :
                heapq.heappop(min_h)
                heapq.heappush(min_h,n)
                heapq.heappush(max_h,-min_h[0])
            else: 
                heapq.heappush(max_h,-n)
        else:
            if min_h[0] > n:
                heapq.heappop(max_h)
                heapq.heappush(max_h,-n)
                heapq.heappush(min_h,-max_h[0])
            else:
                heapq.heappush(min_h,n)
    print(min_h[0])