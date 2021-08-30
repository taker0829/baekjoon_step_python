import sys

case_num = int(sys.stdin.readline())
answer_list = []
output_num = 0

for i in range(1, case_num+1):
    a, b = sys.stdin.readline().split()
    num_a = int(a)
    num_b = int(b)
    answer_list.append(num_a + num_b)

for i in answer_list:
    output_num = output_num + 1
    print("Case #", end='')
    print(output_num, end=": ")
    print(i)