#Number 17(.Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years)

#given sample data
amt = 10000
int = 3.5
years = 7

#formula
future_value = amt * ((1 + (0.01 * int)) ** years)

#output
print("The future value is:", round(future_value, 2))