#Number 20 (Write a Python program to convert height (in feet and inches) to centimeters)

print("Input your height: ")

heightFeet = int(input("Feet: "))

heightInch = int(input("Inches: "))

heightInch += heightFeet * 12
heightCm = round(heightInch * 2.54, 1)

print("Your height is : %d cm." % heightCm)