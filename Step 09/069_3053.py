import math

# Euclid
def Euclid_circle(radius):
    print("{:.6f}".format((radius ** 2) * math.pi))

# Taxi
def Taxi_circle(radius):
    print("{:.6f}".format((radius * 2) ** 2 / 2))

# radius input
r = int(input())
Euclid_circle(r)
Taxi_circle(r)