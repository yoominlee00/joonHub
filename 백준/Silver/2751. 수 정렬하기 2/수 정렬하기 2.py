import sys
num = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readlines()))
lst.sort()
print('\n'.join(map(str, lst)) + '\n')
