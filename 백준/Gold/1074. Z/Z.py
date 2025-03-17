N, x, y = map(int, input().split())
num = 0

def way(N, a, b):
    global num
    if N == 0:
        return
    
    size = 2 ** (N - 1)

    if x < a + size and y < b + size:
        way(N - 1, a, b)
        
    elif x < a + size and y >= b + size:
        num += size * size
        way(N - 1, a, b + size)

    elif x >= a + size and y < b + size:
        num += 2 * size * size
        way(N - 1, a + size, b)
    else:
        num += 3 * size * size
        way(N - 1, a + size, b + size)

way(N, 0, 0)
print(num)
