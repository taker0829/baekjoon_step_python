year = int(input())

# 윤년의 조건
# 1. 4의 배수이면서 100의 배수가 아닐 때
# 2. 400의 배수 일 때
if (year % 400 == 0):
    print("1")
else:
    if (year % 4 == 0) & (year % 100 != 0):
        print("1")
    else:
        print("0")