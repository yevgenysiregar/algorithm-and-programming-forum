#Number 1 (Write a Python program which accepts the radius of a circle from the user and compute the area)

print("This is a program to calculate an area of a circle with a radius that are input by user")

#input radius
radius = float(input("Enter radius: "))

#area of circle formula
phi = 3.14
area = phi * radius * radius

#output
print(f"The area of the circle is : {area}")
