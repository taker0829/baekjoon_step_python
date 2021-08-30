# 입력 번호
ipt_cnt = int(input())
temp_num = 1
num_cnt = 0

while num_cnt < ipt_cnt:
    num_cnt += temp_num
    temp_num += 1
# temp_num - 1(=열의 번호) 가 짝수냐 홀수냐에 따라 시작 지점이 달라짐
# 짝수일 경우 하행선
if ((temp_num - 1) % 2) == 0:
    print(temp_num - (num_cnt - ipt_cnt + 1), '/', num_cnt - ipt_cnt + 1, sep = '')
# 홀수일 경우 상행선
else:
    print(num_cnt - ipt_cnt + 1, '/', temp_num - (num_cnt - ipt_cnt + 1), sep = '')