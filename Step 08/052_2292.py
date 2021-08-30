# 특정 층에 속한 수까지 가는 최소 = 그 단계
# 특정 수 N

ipt_num = int(input())
cycle_num = 0
cycle_temp = 0

while True:
    cycle_temp += cycle_num
    num_temp = 6 * cycle_temp + 1
    if ipt_num <= num_temp:
        print(cycle_num+1)
        break
    cycle_num += 1