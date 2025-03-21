import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
result = []
stack = []
for i in range(N):
    # lst를 하나씩 불러옴.
    # 불러온 값이 더 크다면
    while stack and lst[stack[-1]] <= lst[i]:
        stack.pop()
    if stack:
        result.append(stack[-1]+1)
    else:
        result.append(0)
    stack.append(i)
print(' '.join(map(str,result)))