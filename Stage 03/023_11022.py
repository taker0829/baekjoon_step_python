import sys

case_num = int(sys.stdin.readline())
list_a = []
list_b = []
answer_list = []
output_num = 0

for i in range(1, case_num+1):
    a, b = sys.stdin.readline().split()
    list_a.append(int(a))
    list_b.append(int(b))

for num_a, num_b in zip(list_a, list_b):
    output_num = output_num + 1
    print("Case #", end='')
    print(output_num, end=": ")
    print(num_a, end=" + ")
    print(num_b, end=" = ")
    print(num_a + num_b)