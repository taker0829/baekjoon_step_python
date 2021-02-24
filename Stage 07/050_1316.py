ipt_cnt = int(input())
answer_cnt = 0

for rpt_cnt in range(ipt_cnt):
    temp = None
    ban_list = []
    ipt_str = input()
    for str_part in str(ipt_str):
        if (temp != str_part) & (str_part in ban_list):
            answer_cnt -= 1
            break
        elif (temp != str_part) & (str_part not in ban_list):
            ban_list.append(str_part)
            temp = str_part
        else:
            continue
    answer_cnt += 1
print(answer_cnt)