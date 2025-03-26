import sys
N, K = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().strip()))
stk = []
for i in lst:
    while stk and stk[-1] < i and K > 0:
        stk.pop()
        K -= 1
    stk.append(i)
if K > 0:
    stk = stk[:-K]
print(''.join(map(str,stk)))