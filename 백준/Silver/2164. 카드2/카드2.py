from collections import deque
N = int(input())
lst = list(range(1,N+1))
queue = deque(lst)

while len(queue)>1:
    queue.popleft()
    if queue:
        queue.append(queue[0])
        queue.popleft()

print(queue.popleft())