#Number 10 (Write a Python program to check whether a specified value is contained in a group of values.)

def is_group_member(group_data, n):

   for value in group_data:

       if n == value:

           return True

   return False

x = int(input("Input number: "))

print(is_group_member([1, 5, 8, 3], x))