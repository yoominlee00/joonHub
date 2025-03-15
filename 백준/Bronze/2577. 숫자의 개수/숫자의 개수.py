import sys
a,b,c = map(int,sys.stdin.read().splitlines())
num = [0]*10
for i in list(str(a*b*c)):
    num[int(i)] += 1
list(map(print,num))