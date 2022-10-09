#Number 15 (Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.)

def sumThree(x, y, z):

    if (x == y) or (y == z) or (x==z):

        sum = 0

    else:

        sum = x + y + z

    return sum

firstNumber = int(input("Input first number: "))
secondNumber = int(input("Input second number: "))
thirdNumber = int(input("Input third number: "))

print("The total sum is:", sumThree(firstNumber, secondNumber, thirdNumber))