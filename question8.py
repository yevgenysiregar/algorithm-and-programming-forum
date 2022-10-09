#Number 8 (Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.)

print("This program is to determine whether a number is an odd or an even number.")
anyInteger = int(input("Enter a number: "))

#formula
if (anyInteger % 2 == 0):

    print(f"{anyInteger} is an even number")

else:

    print(f"{anyInteger} is an odd number")