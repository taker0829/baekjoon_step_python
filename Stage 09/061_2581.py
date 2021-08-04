# 첫째/둘째 줄에 입력 M,N. M이상 N 이하의 자연수 중 검색하게 된다.
def Eratos(num_M, num_N):
    # 어차피 1은 소수가 아니기 때문에
    if num_M == 1:
        num_M = 2
    prime_list = [True] * num_N
    
    # M까지의 소수를 구하기 > 에라토스테네스의 체를 활용?
    # 제곱근 까지의 수 -> 해당 수들의 배수를 제외해나가기
    k = int(num_N ** 0.5)
    # 제곱근까지 판별하면 해당 수 소수임 판별 가능?        
    for i in range(2, k+1):
        # 해당 순번이 이미 소수임이 판명됬을 경우
        if prime_list[i-1] == False:
            continue
        else:
            # 최대 점검 가능한 에라토스테네스 순환횟수
            cycle_cnt = num_N // i
            # 해당 횟수만큼 반복, 2부터 시작하여 모두 False 처리 (1일 땐 소수이기 때문)
            for q in range(2, cycle_cnt+1):
                prime_list[(i * q) -1] = False
    
    form_001(prime_list, num_M, num_N)

def form_001(num_list, min_num, max_num):
    prime_sum = 0
    min_prime = 0

    for i in range((max_num - 1), (min_num - 2), -1):
        # 해당 숫자가 소수라면 합과 최소 소수값을 갱신시킨다.
        if num_list[i] == True:
            prime_sum += (i + 1)
            min_prime = (i + 1)
    
    if prime_sum == 0:
        print("-1")
    else:
        print(prime_sum)
        print(min_prime)

inp_M = int(input())
inp_N = int(input())
Eratos(inp_M, inp_N)