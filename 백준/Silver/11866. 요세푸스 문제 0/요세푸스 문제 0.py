from collections import deque
N,K = map(int,input().split())
result = []

lst = list(range(1,N+1))
queue = deque(lst)
n = 0
while queue:
    for _ in range(K-1):
        queue.append(queue[0])
        queue.popleft()
    result.append(queue.popleft())
print(f"<{', '.join(map(str,result))}>")

