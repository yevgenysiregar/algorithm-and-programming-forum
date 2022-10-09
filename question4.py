#Number 4 (Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn)

print("This program is to calculate n + nn + nnn given the n are the input integer")

#input an integer
integer = int(input("Enter an integer: "))

#formula for n + nn + nnn
total = integer + (integer *integer) + (integer*integer*integer)

#output
print(f"Total: {total}")