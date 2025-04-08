import sys
N = int(input())
visited = [False]*N
lst = []
for _ in range(N):
    a, b = map(int,sys.stdin.readline().split())
    lst.append((b,a))
lst.sort()
cnt = 0
for b,a in lst:
    if cnt != 0:
        if a >= end:
            end = b
            cnt += 1
    else:
        end = b
        cnt += 1
print(cnt)