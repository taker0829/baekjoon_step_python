sugar_weight = int(input())

temp = sugar_weight // 5
while True:
    if (temp == 0) and ((sugar_weight % 3) != 0) :
        temp = -1
        break

    rest = sugar_weight - (5 * temp)
    # 나머지가 3으로 나눠 떨어짐
    if (rest % 3) == 0:
        temp += rest // 3
        break
    else:
        temp -= 1
print(temp)