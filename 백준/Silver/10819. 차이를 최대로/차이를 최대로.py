from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

max_sum = 0

for perm in permutations(A):
    total = 0
    for i in range(N - 1):
        total += abs(perm[i] - perm[i + 1])
    max_sum = max(max_sum, total)

print(max_sum)
