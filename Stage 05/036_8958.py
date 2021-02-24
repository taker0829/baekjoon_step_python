import sys

# 입력받는 답안의 갯수
answer_num = int(input())
answer_sheet = []
con = []
temp = 0
count = 0

for k in range(answer_num):
    answer_sheet.append(input())
    con.append(0)

for i in range(answer_num):
    con[i] = 0
    temp = 0
    # 답안지에 대한 점수 계산
    for j in range(len(answer_sheet[i])):
        if answer_sheet[i][j] == 'O':
            temp = temp + 1
            count = count + temp
        else:
            temp = 0
    con[i] = count
    count = 0

for h in range(answer_num):
    print(con[h])