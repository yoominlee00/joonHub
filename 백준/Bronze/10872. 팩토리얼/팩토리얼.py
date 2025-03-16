n =int(input())
def factorial(N):
    if N ==1 or N==0:
        return 1
    return factorial(N-1)*N
print(factorial(n))