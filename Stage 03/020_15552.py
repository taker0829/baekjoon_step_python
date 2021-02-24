import sys
case_num = int(input())
answer_list = []

for i in range(0, case_num):
    a, b = map(int, sys.stdin.readline().split())
    answer_list.append(a+b)

for i in answer_list:
    print(i)