import sys
num_list = []

for i in range(10):
    num_list.append(int(sys.stdin.readline()) % 42)

num_list = set(num_list)
print(len(num_list))