import sys
input = sys.stdin.readline

N = int(input())
f = [0] * 10001

for _ in range(N):
    f[int(input())] += 1 #input 값을 바로 인덱스로 사용해서 올림.

for i in range(1, 10001):
    for _ in range(f[i]):
        sys.stdout.write(f'{i}\n')

