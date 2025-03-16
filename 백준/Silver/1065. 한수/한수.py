input_num = int(input())
num_list = list(range(1,100))
for start in range(1,10):
    for d in range(5):
        if (start- 2*d)<10 and (start-2*d)>=0 and d!=0 : 
            num_minus = start*100 + (start-d)*10 + (start-2*d)
            num_list.append(num_minus)
        if (start+ 2*d)<10 : 
            num_plus = start*100 + (start+d)*10 + (start+2*d)
            num_list.append(num_plus)

if input_num < 100:
    print(input_num)
elif input_num >= 100:
    print(sum(x <= input_num for x in num_list))