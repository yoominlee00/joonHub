import sys
N = int(sys.stdin.readline())
lst =[]
for _ in range(N):
    a = int(sys.stdin.readline())
    if a == 0:
        lst.pop()
    else:
        lst.append(a)
print(sum(lst))