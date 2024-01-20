import math

# The following program needs to prompt the user for two numbers. After the
# user provides the number, the program needs to:
# - add the two numbers together and print the result to the console
# - subtract the two numbers and print the result to the console
# - multiply the two numbers and print the result to the console
# - take the square root (math.sqrt) of each number and print the result to the console
# - multiply each number by math.pi and print the result to the console

# Copy the results of your program into the calculator.txt file

try:
   number_1 = int(input("Enter the first number and hit the [Enter] key: "))
   number_2 = int(input("Enter the second number and hit the [Enter] key: "))

   print("You entered '" + str(number_1) + "' and '" + str(number_2) + "'")

   # addition
   print("Adding '" + str(number_1) + " + " + str(number_2) + "' ...")
   result = number_1 + number_2
   print("Result: '" + str(result) + "'")

   # subtraction
   # TODO: enter code here

   # multiplication
   # TODO: enter code here

   # math.sqrt
   # TODO: enter code here

   # math.pi
   # TODO: enter code here

except Exception as ex:
   print("An error occured. Please try again.")
   print(ex)