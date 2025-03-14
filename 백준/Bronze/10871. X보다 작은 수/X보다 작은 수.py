N, X = map(int, input().split())  
numbers = map(int, input().split())  

print(*filter(lambda num: num < X, numbers))  
