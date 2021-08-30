hour, minute = input().split()
hour = int(hour)
minute = int(minute)

if minute < 45:
    min_sub = minute - 45
    new_min = 60 + min_sub
    if hour == 0:
        new_hour = 23
    else:
        new_hour = hour - 1
else:
    new_min = minute - 45
    new_hour = hour
    
print(new_hour, end=' ')
print(new_min)