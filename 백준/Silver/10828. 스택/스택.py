import sys
N =int(input())
lst=[]
for _ in range(N):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        lst.append(int(a[1]))
    elif a[0] == 'top':
        if not lst:
            print(-1)
        else:
            print(lst[-1])
    elif a[0] == 'size':
        print(len(lst))
    elif a[0] == 'pop':
        if not lst:
            print(-1)
        else:
            print(lst.pop())
    elif a[0] == 'empty':
        if not lst:
            print(1)
        else:
            print(0)