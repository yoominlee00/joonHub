import sys
lst = list(sys.stdin.readline())
N = list(sys.stdin.readline())
lst = lst[:-1]
N = N[:-1]
stk = []
bomb = []
status = False

for i in lst:
    stk.append(i)
    if len(stk) >= len(N):
        if stk[-len(N):] == N:
            for _ in range(len(N)):
                stk.pop()
if stk:
    print(''.join(stk))
else:
    print('FRULA')