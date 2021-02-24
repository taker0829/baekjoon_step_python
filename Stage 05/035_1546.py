import sys

score_num = int(sys.stdin.readline())
score_list = []

score_list = list(map(int, sys.stdin.readline().split()))

max_score = max(score_list)
score_sum = 0

for i in range(score_num):
    score_list[i] = score_list[i]/max_score*100
    score_sum = score_list[i] + score_sum

print(score_sum / score_num)