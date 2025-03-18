import sys

N =int(input())
a = sys.stdin.read().splitlines()
lst = []
for i in list(set(a)):
    lst.append((i,len(i)))

lst.sort(key=lambda x: (x[1], x[0]))

for x in lst:
    print(x[0])