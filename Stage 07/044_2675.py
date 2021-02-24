num_case = int(input())

for rpt_cnt in range(num_case):
    ipt_cnt, ipt_str = input().split()
    str_len = len(ipt_str)
    # index를 먼저 놔야함
    for prt_idx in range(str_len):
        # index를 반복해서 출력
        for prt_rpt in range(int(ipt_cnt)):
            print(ipt_str[prt_idx], end='')
    print('')