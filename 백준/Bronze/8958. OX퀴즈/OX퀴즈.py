N = int(input())
for i in range(N):
    ox_list = list(input())
    score = 0
    plus_score = 0
    for j, value in enumerate(ox_list):
        if value == 'O':
            if j == 0 or ox_list[j-1] != 'O':
                plus_score =1
            else:
                plus_score+=1
        else:
            plus_score =0
        score += plus_score
    print(score)
    