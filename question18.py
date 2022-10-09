#Number 18 (Write a Python program to compute the distance between the points (x1, y1) and (x2, y2))

import math

x = []
x1 = int(input("Enter the first value of x: "))
y1 = int(input("Enter the second value of x: "))
x.append(x1)
x.append(y1)

y = []
x2 = int(input("Enter the first value of y: "))
y2 = int(input("Enter the second value of y: "))
y.append(x2)
y.append(y2)

distance = math.sqrt(((x[0] - y[0]) ** 2)+((x[1] - y[1]) ** 2))

print("The distance between those 2 points are:", distance)