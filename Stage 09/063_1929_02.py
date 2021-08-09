# 첫째/둘째 줄에 입력 M,N. M이상 N 이하의 자연수 중 검색하게 된다.
def Eratos_03(cycle_num):
    # 어차피 1은 소수가 아니기 때문에
    if cycle_num == 1:
        return False
    else:
        # 에라토스테네스의 체 원리에 부합되게, 제곱근까지만 검사해서 지워나가기
        for i in range(2, int(cycle_num ** 0.5) + 1):
            # 나눠떨어지면 즉, 소수가 아니다.
            if cycle_num % i == 0:
                return False
        # 제곱근까지 수를 검사하여 소수임을 판별 완료하면 True return
        return True
        
num_a, num_b = map(int, input().split())
for i in range(num_a, num_b+1):
    if Eratos_03(i):
        print(i)