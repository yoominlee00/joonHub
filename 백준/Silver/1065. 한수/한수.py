input_num = int(input())
lst = []
for num in list(range(1,1001)):
    if len(list(str(num)))== 1 or len(list(str(num)))== 2:
        lst.append((num))
    elif len(list(str(num)))==3:
        a,b,c = map(int,list(str(num)))
        if a-b == b-c:
            lst.append(num)
if input_num < 100:
    print(input_num)
elif input_num >= 100:
    print(sum(x <= input_num for x in lst))