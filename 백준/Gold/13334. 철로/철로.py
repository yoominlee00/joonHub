import sys
import heapq
N = int(sys.stdin.readline())
lst = []
train = []
cnt = 0

for _ in range(N):
    h, o = map(int,sys.stdin.readline().split())
    H = min(h,o)
    O = max(h,o)
    heapq.heappush(lst,(O,H))
d = int(sys.stdin.readline())

while lst:
    end = heapq.heappop(lst)
    heapq.heappush(train,end[1])
    while train[0] < (end[0]-d):
        heapq.heappop(train)
        if not train:
            break
    if len(train) >= cnt:
        cnt = len(train)

print(cnt)
    