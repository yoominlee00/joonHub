from collections import deque
import sys

queue = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    l = sys.stdin.readline().split()
    if l[0] == 'push':
        queue.append(int(l[1]))
    elif l[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif l[0] == 'size':
        print(len(queue))
    elif l[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif l[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif l[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])