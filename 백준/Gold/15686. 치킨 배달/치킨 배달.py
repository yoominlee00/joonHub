import sys 
from itertools import combinations
from collections import deque

N, M = map(int,sys.stdin.readline().split())
maps = [ list(map(int,sys.stdin.readline().split())) for _ in range(N) ]

chickens = [(x,y) for x in range(N) for y in range(N) if maps[x][y] == 2]
homes = [(x,y) for x in range(N) for y in range(N) if maps[x][y] == 1]

max_total = float('inf')
for ch in combinations(chickens,M):
    total = 0
    for h_x, h_y in homes:
        min_distance = float('inf')
        for x,y in ch:
            distance = abs(x-h_x) +  abs(y-h_y)
            min_distance = min(distance, min_distance)
        total += min_distance
    max_total = min(total,max_total)
print(max_total)