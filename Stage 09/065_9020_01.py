# 에라토스테네스
def Eratos_04_mod(n):
    n += 1                            # for문 사용을 위한 n += 1
    prime = [True] * n                # n개의 [True]가 있는 리스트 생성
    num_list = []
    for i in range(2, int(n**0.5)+1): # n의 제곱근까지만 검사
        if prime[i]:                    # prime[i]가 True일때
            for j in range(2*i, n, i):    # prime 내 i의 배수들을 False로 변환
                prime[j] = False
    
    # 소수를 선별 저장
    for i in range(1, n):
        if prime[i] is True:
            num_list.append(i)

    goldbach(n-1, num_list)

# 소수 리스트의 중간부터 index 줄여나가며 계산 수행 -> 틀린 방식
# 소수 리스트 중 num값의 절반에 가장 근접한 값을 찾아햐 함
def goldbach(num, prime_list):
    key_idx = index_cnt(num // 2, len(prime_list) // 2, prime_list)
    for i in range(key_idx, -1, -1):
        pair_num = num - prime_list[i]
        # 소수 페어가 존재할 경우, 해당 수가 정답
        if pair_num in prime_list:
            if prime_list[i] <= pair_num:
                answer_sheet.append(prime_list[i])
                answer_sheet.append(pair_num)
            else:
                answer_sheet.append(pair_num)    
                answer_sheet.append(prime_list[i])
            break

def index_cnt(key_num, str_idx, num_list):
    num_gap = abs(key_num - num_list[str_idx])
    compare_A = abs(key_num - num_list[str_idx + 1])
    compare_B = abs(key_num - num_list[str_idx - 1])
    cnt_flag = min(compare_B, num_gap, compare_A)

    # Python 재귀함수에서의 return값 처리
    if (cnt_flag == compare_B) and (compare_B != num_gap):
        #print("왼쪽으로 index 이동")
        return index_cnt(key_num, str_idx - 1, num_list)
    elif (cnt_flag == compare_A) and (compare_A != num_gap):
        #print("오른쪽으로 index 이동")
        return index_cnt(key_num, str_idx + 1, num_list)
    else:
        #print("Key Index")
        return(str_idx)

# 첫째 줄에 테스트 케이스 t 입력
t = int(input())
inp_list = [0] * t
true_key = 0
answer_sheet = []
# 입력받은 테스트 케이스 수 만큼 입력 재수행
for i in range(t):
    # 입력 값 수행
    inp_list[i] = int(input())
    # 해당 값들을 바탕으로 에라토스테네스의 체 수행 후, 해당 소수 리스트를 사용하여 골드바흐 계산
    Eratos_04_mod(inp_list[i])

for i in range(len(answer_sheet)):
    cnt = i + 1
    if cnt % 2 == 0:
        print(answer_sheet[i])
    else:
        print(answer_sheet[i], end=' ')