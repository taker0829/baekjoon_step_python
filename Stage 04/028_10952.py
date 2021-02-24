import sys

answer_list = []

while True:
    string_a, string_b = sys.stdin.readline().split()
    int_a = int(string_a)
    int_b = int(string_b)

    if (int_a == 0) & (int_b == 0):
        break

    answer_list.append(int_a + int_b)

for i in range(0, len(answer_list)):
    print(answer_list[i])