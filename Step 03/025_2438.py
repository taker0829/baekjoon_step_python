import sys

line_cnt = int(sys.stdin.readline())

for i in range(1, line_cnt+1):
    for j in range(0, i):
        print("*", end='')
    print("")