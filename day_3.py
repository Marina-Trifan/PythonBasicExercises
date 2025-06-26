"""
Exercise 1:
You have a number 'n'. Display all even numbers from 0 to 20 using 'continue'
"""
n = 0      # initialize the variable 'n' to 0, which will be used to track the current number in the loop
while n < 21:   # start a while loop that continues as long as 'n' is lower than 21
    n += 1      # increment 'n' by 1 on each loop iteration
    if n %2 == 1:   # check if 'n' is an even or odd number
        continue    # if 'n' is an odd number: continue
    print(n)        # display only the even numbers

# to display also 0:
n = -1       # initialize the variable 'n' to -1, which will be used to track the current number in the loop
while n < 21:   # start a while loop that continues as long as 'n' is lower than 21
    n += 1      # increment 'n' by 1 on each loop iteration
    if n %2 == 1:   # check if 'n' is an even or odd number
        continue    # if 'n' is an odd number: continue
    print(n)        # display only the even numbers

print("\n")

"""
Exercise 2:
Write a Python program that:
- Asks the user for their grade (0-100).
- Prints "Pass" if the grade is 50 or higher, and "Fail" if it is below 50.
- If the grade is above 90, print "Excellent" instead of "Pass."
"""
user_input = int(input("Type your grade: "))   # ask the user for a grade

if user_input >= 50 and user_input < 90:      # if the user's grade is between 50 and 90 display 'Pass'
      print("Pass")
elif user_input >= 90:                        # if the user's grade is greater than 90 display 'Excellent'
      print("Excellent")
elif user_input < 50:                         # if the user's grade is lower than 50 display 'Fail'
      print("Fail")

print("\n")

"""
Exercise 3: 
Write a Python program that:
- Asks the user to input a number.
- Prints whether the number is "Even" or "Odd."
"""

number = int(input("Type a number of your choice: "))    # ask the user for a number
if number % 2 == 0:                      # if the remaining of the division (number/2) = zero, display EVEN
      print (f"Number {number} is an EVEN number")
else:                                    # else: the remaining of the division (number/2) is not zero, display ODD
      print(f"Number {number} is an ODD number.")

print("\n")

"""
Exercise 4:
Write a Python program that:
- Asks the user for a positive integer.
- Calculates and prints its factorial using a while loop.
"""

positive_integer = int(input("Type a positive integer number: "))   # ask the user for a positive integer
factorial = 1            # not to use the math module, declare a variable 'factorial' with the initial value '0'
while positive_integer > 0:       # calculate and display the positive integer factorial using a 'while' loop
      factorial *= positive_integer
      positive_integer -= 1
      print(f"{factorial} is the factorial for {positive_integer}")

print("\n")

"""
Exercise 5: 
Write a Python program that:
- Asks the user to input a number.
- Prints the multiplication table for that number (from 1 to 10) using a for loop.
"""

number = int(input("Type a number: "))     # ask the user for a numer
for i in range(1, 11):
      print(f"{number}x{i} = {number * i}")   # display the multiplication table for that number, from 1 to 10

print("\n")

"""
Exercise 6:
Write a Python program that:
- Asks the user for two numbers, a start and an end.
- Calculates and prints the sum of all numbers in the range (inclusive) using a for loop.
"""

start_number = int(input("Type a start number: "))   # ask the user for the start number
end_number = int(input("Type an end number: "))      # ask the user for the end number

sum_numbers = 0   # create a variable to hold the sum

for number in range(start_number, end_number + 1):  # add the '+ 1' to include also de end_number
      sum_numbers += number         # add the numbers from the range
print(f"The sum of numbers from {start_number} to {end_number} is: {sum_numbers}")    # print the result

print("\n")

"""
Exercise 7:
Write a Python program that:
- Prints numbers from 1 to 50.
- For multiples of 3, print "Fizz" instead of the number.
- For multiples of 5, print "Buzz" instead of the number.
- For multiples of both 3 and 5, print "FizzBuzz."
"""

for number in range(1,51):     # use a for loop to print numbers from 1 to 50, including 50
      if number % 3 == 0 and number % 5 == 0:     # if the number is a multiple of 3 and 5, display 'FizzBuzz'
            print("FizzBuzz")
      elif number % 3 == 0:                       # if the number is only a multiple of 3, display 'Fizz'
            print("Fizz")
      elif number % 5 == 0:                       # if the number is only a multiple of 5, display 'Buzz'
            print("Buzz")
      else:
            print(f"{number}")

print("\n")

"""
Exercise 8:
Write a Python program that:
- Randomly selects a number between 1 and 100 (you can hardcode it for now).
- Allows the user to guess the number, providing hints like "Too high" or "Too low."
- Ends when the user guesses the correct number.
"""
import random        # import the random library in order to generate a random number

number = random.randint(1, 100)   # declare a variable that takes a random value from 1 to 100
while True:        # since the number of iterations a while loop is used
      user_input = int(input("Type your guess: "))     # ask the user to guess the number
      if user_input > number:            # if the user input is greater than the random number display 'Too high'
            print("Too high")
      elif user_input < number:          # if the user input is lower than the random number display 'Too low'
            print("Too low")
      else:
            print("Your answer is correct")    # else the user input is correct display 'Your answer is correct'
            break                              # and break (exit) the loop

print("\n")

"""
Exercise 9: 
Write a Python program that:
Uses for loop to print the following pattern:
*
**
***
****
*****
"""

for i in range (1, 6):   # a for loop was used to print the above pattern
      print(i*"*")

print("\n")

"""
Exercise 10:
Write a program that:
- Asks the user to input a list of numbers (separated by spaces).
- Finds and prints the largest number in the list.
"""
# ask the user for a string of numbers and use the split() function to separate it into a list of strings
list_of_numbers = input("Type a list of numbers separated by spaces: "). split()
print(list_of_numbers)       # display the list
for index, number in enumerate(list_of_numbers):      # enumerate(list_of_numbers) gives the index and the value
                                                      # of each item in the list
      list_of_numbers[index] = int(number)            # convert each number (currently a string) into an integer
print(f"The largest number is: {max(list_of_numbers)}")    # display the largest number using the 'max()' function

print("\n")

"""
Exercise 11:
Write a program that:
- Asks the user to input the number of rows.

- Prints the following triangle pattern using numbers:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

rows = int(input("Type the number of rows: "))  # ask the user to input a number of rows
for i in  range(1, rows + 1):      # starts a loop from 1 to 'rows' (inclusive),
                                   # where 'i' represents the current row number
      for j in range (1, i + 1):   # inner loop from 1 to 'i' (inclusive),
                                   # where j represents the number to be printed in that row
            print(j, end = " ")    # display the value of 'j', where 'end' prevents the cursor from moving
                                   # to the next line after each print
      print()                      # after each row is printed, this moves the cursor to the next line