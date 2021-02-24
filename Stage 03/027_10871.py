import sys

num_list = []

# 처음 입력 수 갯수 & 기준 number 입력
origin_n, origin_x = sys.stdin.readline().split()
int_n = int(origin_n)
int_x = int(origin_x)

input_list = sys.stdin.readline().split()

# 입력 수 갯수와 다를 겨우 예외 처리
if int_n != len(input_list):
    print("Error Occured!")
else:
    for i in range(0, int_n):
    	# 판단 기준, int_x보다 작을 경우
        if int(input_list[i]) < int_x:
            print(int(input_list[i]), end=" ")
        else:
            print("", end="")