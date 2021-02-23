base_num = int(input())
multiply_num = int(input())

# 1단계. 자릿수로 분해
multiply_a = multiply_num // 100
multiply_b = multiply_num % 100 // 10
multiply_c = multiply_num % 10

cal_a = base_num * multiply_a
cal_b = base_num * multiply_b
cal_c = base_num * multiply_c

print(cal_a)
print(cal_b)
print(cal_c)
print(100 * cal_a + 10 * cal_b + cal_c)