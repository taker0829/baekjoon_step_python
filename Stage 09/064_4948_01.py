# 가장 큰 수만 사용해서 체를 적용
def Eratos_05(base_num):
    prime_cnt = 0
    m = base_num
    n = base_num * 2 + 1
    # n개의 [True]가 있는 리스트 생성
    prime_list = [True] * n

    # n의 제곱근까지만 검사
    for i in range(2, int(n ** 0.5)+1) :
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
Eratos_05(max(inp_list))