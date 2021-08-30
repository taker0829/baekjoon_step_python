import sys

def calc_process(num_a, num_b):
    num_part = num_a + num_b
    if num_part > 10 :
        con = str(num_b) + str(num_part)[1]
        return con
    else :
        con = str(num_b) + str(num_part)[0]
        return con

origin_num = str(sys.stdin.readline())
con_num = 0
cycle_cnt = 0

if (len(origin_num) == 2):
    con_num = origin_num.zfill(3)
elif (len(origin_num) == 1):
    print("Error Occured")
else:
    con_num = origin_num

while True:
    num_a = int(con_num[0])
    num_b = int(con_num[1])
    con_num = calc_process(num_a, num_b)
    cycle_cnt = cycle_cnt + 1
    
    if (int(con_num) == int(origin_num)):
        break

print(cycle_cnt)