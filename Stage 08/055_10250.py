test_case = int(input())
answer_list = []

# H : 호텔 층 수, W : 각 층 방의 수, N : 손님의 번호
# 수직으로 열을 먼저 채우고 넘어가는 방식
for cycle_num in range(test_case):
    ipt_H, ipt_W, ipt_N = map(int, input().split())

    if (ipt_N // ipt_H) < 1:
        floor_str = str(ipt_N)
        room_str = str(1).zfill(2)
        answer_list.append(floor_str + room_str)
    else:
        if (ipt_N % ipt_H) == 0:
            floor_str = str(ipt_H)
            room_str = str(ipt_N // ipt_H).zfill(2)
        else:
            floor_str = str(ipt_N % ipt_H)
            room_str = str(ipt_N // ipt_H + 1).zfill(2)
       
        answer_list.append(floor_str + room_str)

for answers in answer_list:
    print(answers)