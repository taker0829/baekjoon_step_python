import sys

num_A = int(sys.stdin.readline())
num_B = int(sys.stdin.readline())
num_C = int(sys.stdin.readline())

num_Con = num_A * num_B * num_C
str_Con = str(num_Con)

for i in range(10):
    print(str_Con.count(str(i)))