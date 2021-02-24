# 계산에 활용하기 위한 2가지 집합을 선언
origin_num = set(range(1, 10001))
self_num = set()

for i in range(1, 10001):
    # 1 ~ 10000의 값 i를 str 처리시켜서 한 글자씩 활용
    for j in str(i):
        # 생성자 계산 방식을 위함
        i = i + int(j)
    self_num.add(i)

# set는 서로 '-' 연산을 수행함을 통해 차이만 남길 수 있다
non_self_num = origin_num - self_num

for answer in sorted(non_self_num):
    print(answer)