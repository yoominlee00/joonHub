import sys
import bisect
from collections import deque

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst = deque(lst)
stack = deque()

while lst:
    a = lst[0]
    index = bisect.bisect_left(stack,a)
    if index < len(stack):
        stack[index] = a 
    else:
        stack.append(a)
    lst.popleft()
print(len(stack))
    