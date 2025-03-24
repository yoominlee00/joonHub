import sys

A, B, C = map(int,sys.stdin.readline().split())
def mul(b):
    if b == 1:
        return A % C
    
    if b % 2 == 0:
        val = mul(b//2)
        return val**2%C
    else:
        val1 = mul(b//2)
        return (val1**2*A)%C
print(mul(B))