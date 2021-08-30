# 첫째/둘째 줄에 입력 M,N. M이상 N 이하의 자연수 중 검색하게 된다.
def Eratos_02(num_M, num_N):
    # 어차피 1은 소수가 아니기 때문에
    prime_list = [i for i in range(2, num_N+1)]
    # M까지의 소수를 구하기 > 에라토스테네스의 체를 활용?
    # 제곱근 까지의 수 -> 해당 수들의 배수를 제외해나가기
    for i in range(2, int(num_N ** 0.5) + 1):
        if i in prime_list:
            #에라토스테네스의 체 원리에 가장 부합
            for j in range(i*2, num_N+1, i):
                if j in prime_list:
                    prime_list.remove(j)  

    print_form(prime_list, num_M, num_N)

def print_form(num_list, min_num, max_num):
    for i in range(len(num_list)):
        if num_list[i] >= min_num and num_list[i] <= max_num:
            print(num_list[i])

num_a, num_b = map(int, input().split())
Eratos_02(num_a, num_b)