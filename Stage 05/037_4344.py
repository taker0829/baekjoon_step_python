test_case = int(input())
answer_sheet = []

for i in range(test_case):
    count = 0
    # 입력 받는 값을 int의 list로
    input_list = list(map(int, input().split()))
    mean = (sum(input_list) - input_list[0]) / (len(input_list) - 1)

    for j in range(1, len(input_list)):
        if input_list[j] > mean:
            count += 1

    print('%.3f' % ((count/(len(input_list) - 1)) * 100), end='%\n')