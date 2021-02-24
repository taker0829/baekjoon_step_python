# A, 생산 고정비용
# B, 제품 수당 생산비용
# C, 제품 판매가
ipt_A, ipt_B, ipt_C = map(int, input().split())
# 손익분기점이 발생하는 최소조건, 제조비용 < 판매비용
# 추가로 고려해야할 최소조건, 고정비용 이상에서 시작해야함
if ipt_B >= ipt_C:
    BEP_cnt = -1
    print(BEP_cnt)
else:
    BEP_cnt = ipt_A // (ipt_C - ipt_B)
    print(BEP_cnt+1)