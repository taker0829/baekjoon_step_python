import sys

line_cnt = int(sys.stdin.readline())

for i in range(1, line_cnt+1):
    # line_cnt-i 를 통해서 앞에 빈칸을 생성
    # 이걸 우측정렬을 통해 풀 수 있을까?
    print("".ljust(line_cnt-i), end='')
    for j in range(0, i):
        print("*", end='')
    print("")