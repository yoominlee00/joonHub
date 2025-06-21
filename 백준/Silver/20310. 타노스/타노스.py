lst =  list(map(int,input()))
num_1 = sum(lst)
num_0 = len(lst)-num_1
print('0'*(num_0//2)+'1'*(num_1//2))