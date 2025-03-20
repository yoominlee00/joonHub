import sys
N =int(sys.stdin.readline())
for _ in range(N):
    l = []
    lst = list(sys.stdin.readline())
    for i in lst:
        if i == '(': 
            l.append('(')
        elif i == ')' and not l: 
            print('NO')
            break
        elif i == ')' and l:
            l.pop()
    else:
        if not l:
            print('YES')
        else:
            print('NO')

