#Number 14 (Write a Python program to get the least common multiple (LCM) of two positive integers.)

def computeLcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

firstNumber = int(input("Input first number: "))
secondNumber = int(input("Input second number: "))

print("The L.C.M. is:", computeLcm(firstNumber, secondNumber))