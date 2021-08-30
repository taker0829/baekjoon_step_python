# 가장 큰 수만 사용해서 체를 적용
def Eratos_06(base_num):
    n = base_num * 2 + 1
    # n개의 [True]가 있는 리스트 생성
    prime_list = [True] * n
    for i in range(n):
        if (i % 2 == 0):
            prime_list[i] = False

    # 2만 예외처리
    prime_list[2] = True
    # n의 제곱근까지만 검사
    # 어차피 짝수는 소수가 될 수 없다 (2 제외)
    for i in range(3, int(n ** 0.5)+1, 2) :
        # prime[i]가 True일때
        if prime_list[i] :
            # prime 내 i의 배수들을 False로 변환
            for j in range(2 * i, n, i) :
                prime_list[j] = False
    cnt_prime(inp_list, prime_list)

def cnt_prime(input, prime):
    prime_cnt = 0

    for i in range(len(input)):
        min = input[i] + 1
        max = input[i] * 2 + 1

        for i in range(min, max):
            if i > 1 and prime[i] == True :
                prime_cnt += 1
        print(prime_cnt)
        prime_cnt = 0

inp_list = []
while True :
    new_inp = int(input())
    if new_inp == 0 :
        break
    else :
        inp_list.append(new_inp)
Eratos_06(123456)