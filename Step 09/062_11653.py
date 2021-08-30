def prime_facto(inp_num):
    sqrt_num = int(inp_num ** 0.5)
    #print(sqrt_num)
    cycle_num = inp_num
    # 입력이 1일 때는 바로 종료
    if inp_num == 1:
        exit()
    # 제곱근 영역까지 소수 판별
    for i in range(2, sqrt_num+1):
        while inp_num % i == 0:
            print(i)
            inp_num /= i
    if int(inp_num) != 1:
        print(int(inp_num))


input_num = int(input())
prime_facto(input_num)