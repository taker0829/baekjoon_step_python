import sys

while True:
    try:
        int_a, int_b = map(int, sys.stdin.readline().split())
        print(int_a + int_b)
    except:
        break