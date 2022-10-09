#Number 7 (. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.)

firstNumber = int(input("Enter a number: "))
secondNumber = int(input("Enter a number: "))
thirdNumber = int(input("Enter a number: "))

#formula
total = firstNumber + secondNumber + thirdNumber

if (firstNumber == secondNumber == thirdNumber):

    print("The first, second and third number are the same")
    print("so the result is the total addition of all the input number times 3")
    print(f"Result: {total * 3}")

else:
    print("The first, second and third number are NOT the same")
    print("so the result is the total addition of all the input number")
    print(f"Result: {total}")