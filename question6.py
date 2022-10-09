#Number 6 (Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

print("This program is to know the difference between the input number and 17")
print("But if the input number is more than 17, the difference between the input number and 17 is times by 2")
randomNumber = int(input("Enter a number: "))

#formula
difference = abs(17 - randomNumber)

if (randomNumber > 17):

    print(difference * 2)

else:

    print(f"The difference between {randomNumber} and 17 are: {difference}")