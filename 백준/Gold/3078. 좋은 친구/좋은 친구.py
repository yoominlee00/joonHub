import sys 
N, K = map(int,input().split())
all_friends = list(sys.stdin.read().split())


good_friend = 0
same_len = [0]*21

for i in range(N):
    new = len(all_friends[i])
    if same_len[new] != 0:
        good_friend += same_len[new]
    same_len[new] += 1

    if i < K:
        continue
    else:
        last = len(all_friends[i-K])
        same_len[last] -= 1

print(good_friend)