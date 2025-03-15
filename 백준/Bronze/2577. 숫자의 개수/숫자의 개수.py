import sys
a,b,c = map(int,sys.stdin.read().splitlines())
num = [0]*10
value = str(a*b*c)
for i in list(value):
    num[int(i)] += 1
list(map(print,num))