#Number 9 (Write a Python program to test whether a letter is a vowel or not)

vowels = ["a", "i", "e", "o", "u"]

letter = input("Enter a letter: ")
letter = letter.lower()

if (letter in vowels):

    print(f"{letter} is a vowels")

else:

    print(f"{letter} is NOT a vowels")
