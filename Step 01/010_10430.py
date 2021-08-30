a, b, c = input().split()

num_a = int(a)
num_b = int(b)
num_c = int(c)

form_001 = (num_a + num_b) % num_c
form_002 = ((num_a % num_c) + (num_b % num_c)) % num_c
form_003 = (num_a * num_b) % num_c
form_004 = ((num_a % num_c) * (num_b % num_c)) % num_c

print(form_001)
print(form_002)
print(form_003)
print(form_004)