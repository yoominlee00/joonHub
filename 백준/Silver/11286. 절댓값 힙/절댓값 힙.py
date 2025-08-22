
import heapq

N = int(input())
lst = []
for _ in range(N):
    n = int(input())
    if n != 0:
        heapq.heappush(lst,(abs(n),n))
    else:
        if not lst:
            print(0)
            continue
        output = heapq.heappop(lst)
        print(output[1])

