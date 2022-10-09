#Number 21 (Write a Python program to calculate the hypotenuse of a right angled triangle)

import math

bcLength = int(input("Input length BC: "))
abLength = int(input("Input length AB: "))

hypotenuse = math.sqrt(bcLength ** 2 + abLength ** 2)

print("The hypotenuse of right triangle ABC is:", hypotenuse)