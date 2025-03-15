case_num = int(input())
for i in range(case_num):
    std = list(map(int,input().split()))
    avg = sum(std[1:])/std[0]
    avg_over_rate = round(sum([x > avg for x in std[1:]])/std[0]*100,3)
    print(format(avg_over_rate,".3f")+"%")