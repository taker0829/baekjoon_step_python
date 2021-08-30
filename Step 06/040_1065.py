try_num = int(input())

if try_num < 100:
    count = try_num
else:
    count = 99
    for cycle_num in range(100, try_num+1):
        num_001 = cycle_num // 100
        num_002 = (cycle_num % 100) // 10
        num_003 = cycle_num % 10
        if (num_002 - num_001) == (num_003 - num_002):
            count += 1

print(count)