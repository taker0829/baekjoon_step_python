answer_list = []

def pythagoras(num_001, num_002, num_003):
    inp_list = [num_001, num_002, num_003]
    max_num = max(inp_list)
    max_idx = inp_list.index(max_num)
    del inp_list[max_idx]

    if max_num ** 2 == inp_list[0] ** 2 + inp_list[1] ** 2:
        return("right")
    else:
        return("wrong")

while True:
    a, b, c = map(int, input().split())
    if (a == 0 & b == 0 & c == 0):
        break
    answer_list.append(pythagoras(a, b, c))

for k in answer_list:
    print(k)