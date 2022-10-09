#Number 22 (Write a Python program to calculate body mass index)

height = float(input("Input your height in Meters: "))
weight = float(input("Input your weight in Kilogram: "))

bodyMassIndex = round(weight / (height * height), 2)

print("Your body mass index is:", bodyMassIndex)