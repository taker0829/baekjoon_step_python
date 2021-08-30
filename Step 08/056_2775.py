test_case = int(input())

for case_loop in range(test_case):
    # k는 목표 층, n은 목표 호수
    k = int(input())
    n = int(input())

    people_list = [i for i in range(1, n+1)]
    for floor in range(k):
        for room in range(1, n):
            # 바꿀 값 = 바꿀 위치의 기존 값 + 바뀐 직전 값 (= 해당 위치까지의 합)
            people_list[room] = people_list[room - 1] + people_list[room]
    print(people_list[-1])