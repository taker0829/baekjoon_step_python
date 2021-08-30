test_case = int(input())
num_list = []

if test_case == 0:
    print("Exception Occured")

for i in range(0, test_case):
    a, b = input().split()
    num_a = int(a)
    num_b = int(b)
    num_list.append(num_a+num_b)

for i in range(0, test_case):
    print(num_list[i])