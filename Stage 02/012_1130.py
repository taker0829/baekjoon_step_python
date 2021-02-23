a, b = input().split()

num_a = int(a)
num_b = int(b)

if num_a > num_b:
    print(">")
elif num_a < num_b:
    print("<")
else:
    print("==")