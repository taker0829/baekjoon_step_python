import math
# A : 낮에 등반 높이, B : 밤동안 추락 높이, V : 총 막대 높이
ipt_A, ipt_B, ipt_V = map(int, input().split())

# 도착하는 날에는 추락은 계산 X
height_temp = (ipt_V - ipt_B)
print(math.ceil(height_temp / (ipt_A - ipt_B)))