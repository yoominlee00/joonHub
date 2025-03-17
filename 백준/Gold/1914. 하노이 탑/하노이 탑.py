N = int(input())
result = []

def hanoi(n, start, end):
    if n > 0:
        mid = 6 - start - end
        hanoi(n-1, start, mid)
        print(f"{start} {end}")
        hanoi(n-1, mid, end)

print(2**N - 1)
if N<=20:
    hanoi(N, 1, 3)

