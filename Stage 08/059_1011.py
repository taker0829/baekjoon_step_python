import math

for _ in range(int(input())):
    start_x, end_y = map(int, input().split())
    distance = end_y - start_x
    key_k = math.trunc(math.sqrt(distance - 1))
    print( 2 * key_k + 1 if distance > key_k ** 2 + key_k else 2 * key_k)