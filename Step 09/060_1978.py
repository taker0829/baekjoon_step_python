#import math
import sys
# 첫 줄에 숫자 개수를 입력
input_cnt = int(input())
# 입력된 숫자 개수만큼 숫자들 입력
int_list = list(map(int, input().split()))
if input_cnt < len(int_list):
    sys.exit('Error, input limitation over')

prime_cnt = 0

for int_cycle in int_list :
    # flag 초기화
    flag = True
    # 1은 소수가 아님
    if int_cycle <= 1:
        flag = False
    # 짝수는 애초에 소수가 아님. But, 2는 예외
    elif int_cycle % 2 == 0:
        if int_cycle == 2:
            flag = True
        else:
            flag = False
    # 제곱근까지 정수를 차례로 나눠보면서 한 번이라도 나눠떨어지면 해당 수는 소수가 아님       
    #mid_num = math.log2(int_cycle)
    mid_num = round(int_cycle ** 0.5) + 1
    # range의 3번재 인자는 숫자 사이의 거리를 뜻 = 어차피 짝수는 소수일 수가 없기 때문에
    for i in range(3, mid_num, 2):
        if (int_cycle % i) == 0:
            flag = False
            break
    # 제곱근까지 순회하면서 확인 결과 나누어떨어지는 것이 존재하지 않는다면
    if flag == True:
        prime_cnt += 1
print(prime_cnt)    