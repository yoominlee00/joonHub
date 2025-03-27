import sys
from collections import deque
N = int(input())
for _ in range(N):
    N, M = map(int,sys.stdin.readline().split())
    lst = list(map(int,sys.stdin.readline().split()))
    pri = sorted(lst)
    id = deque(list(range(N)))
    cnt = 0
    pop_id = None
    
 
    while lst:
        while lst[id[0]] != pri[-1]:
            a = id.popleft()
            id.append(a)

        if lst[id[0]] == pri[-1]:
            pop_id = id.popleft()
            pri.pop()
            cnt +=1
        
        if pop_id == M:
            print(cnt)
            break
            
    
   