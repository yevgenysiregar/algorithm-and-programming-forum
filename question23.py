#Number 23 (Write a Python program to calculate midpoints of a line)

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

z = []
z1 = (x1 + x2) / 2
z2 = (y1 + y2) / 2
z.append(z1)
z.append(z2)

print("The midpoints of the line is:", z)