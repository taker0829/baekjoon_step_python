import sys

# 입력 수 갯수
input_num = int(sys.stdin.readline())
# 숫자 맞게 입력
num_list = list(map(int, sys.stdin.readline().split()))

# 예외 처리 딱히 언급 없으니 걍 넘김
print('{} {}'.format(min(num_list), max(num_list)))