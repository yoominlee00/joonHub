import sys
T = int(input())
for _ in range(T):
    N = int(input())
    lst = []
    for _ in range(N):
        a, b = map(int,sys.stdin.readline().split())
        lst.append((a,b))
    lst.sort()
    y_limit = lst[0][1]
    cnt = 0
    for x, y in lst:
        if y_limit >= y:
            cnt += 1
            y_limit = y
    print(cnt)