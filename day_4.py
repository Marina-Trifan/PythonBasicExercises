"""
Exercise 1:
Cube of a Number: Write a function called cube that takes a number as a parameter and returns its cube (the
number raised to the power of 3).

Example:
print(cube(3))  # Output: 27
"""

def cube(number):        # created function cube that takes 'number' as a parameter
    return number ** 3   # and returns its cube

print(cube(3))       # calling the function 'cube'


print("\n")  # new line in the terminal

"""
Exercise 2:
Concatenate Strings: Write a function concatenate_strings that takes two strings as parameters and returns their
concatenation.

Example:
result = concatenate_strings("Hello", "World")
print(result)  # Output: HelloWorld
"""

def concatenate_strings(string_1, string_2):  # function cube created and it takes 2 strings as parameters
    return string_1 + string_2                # the function returns the concatenation of the 2 strings


print(concatenate_strings("First string and ", "second string"))  # first call of the function

# or as in the example from the exercise:
result = concatenate_strings("Second example ", "of string concatenation")  # second call
print(result)


print("\n")  # new line in the terminal

"""
Exercise 3:
Count the Number of Characters: Write a function count_characters that takes a string as a parameter and returns
the number of characters in the string (excluding spaces).

Example:
print(count_characters("Hello World"))  # Output: 10
"""

def count_characters(a_string):              # define the function count_characters
    return len(a_string.replace(" ", ""))    # the function returns the total number of characters without spaces


print(count_characters("This is a string."))   # calling the count_characters function


print("\n")  # new line in the terminal

"""
Exercise 4:
Convert Minutes to Hours: Write a function called convert_minutes_to_hours that takes an integer representing
minutes and returns the number of hours and minutes.

Example:
print(convert_minutes_to_hours(150))  # Output: 2 hours and 30 minutes
"""

def convert_minutes_to_hours(number):     # define the function convert_minutes_to_hours
    hours = number // 60                  # transform 'number' from minutes to hours
    minutes = number % 60                 # calculate the remaining minutes from 'number'

    return f" {hours} hours and {minutes} minutes"   # the function returns the number of hours and minutes


print(convert_minutes_to_hours(167))   # calling the convert_minutes_to_hours function


print("\n")  # new line in the terminal

"""
Exercise 5:
Find the Length of a List: Write a function called list_length that takes a list as a parameter and returns the
number of items in the list.

Example:
print(list_length([1, 2, 3, 4]))  # Output: 4
"""

def list_length(a_list):     # define the function 'list_length' that takes as a parameter a list
    return f"The number of items in the list is: {len(a_list)}"   # returns the length of the list

print(list_length([1, "item", - 3, "item", 4.13, True]))  # calling the function 'list_length'


print("\n")  # new line in the terminal

"""
Exercise 6:
Divide Two Numbers: Write a function divide_numbers that takes two numbers as parameters and returns their
division result. If the second number is zero, return a message "Cannot divide by zero."

Example:
print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(10, 0))  # Output: Cannot divide by zero
"""

def divide_numbers(number_1, number_2):    # define the function divide_numbers
    if number_2 != 0:                      # if 'number_2' is not zero return the numbers division
        print(f"The numbers division result is: {number_1 / number_2}")
    else:                                  # if 'number_2'  is zero return the message "Cannot divide by zero."
        print(f"Cannot divide by zero.")

divide_numbers(1, 2)   # calling the function divide_Number function, when 'number_2' is not zero
divide_numbers(1, 0)   # calling the function divide_Number function, when 'number_2' is zero


print("\n")  # new line in the terminal

"""
Exercise 7:
Find the Average of a List: Write a function average that takes a list of numbers and returns their average
(sum divided by the number of elements).

Example:
print(average([10, 20, 30, 40]))  # Output: 25.0
"""

def average(a_list_of_numbers):    # define the function 'average' that takes a list of numbers as an argument
    return sum(a_list_of_numbers) / len(a_list_of_numbers)   # the function returns the average of the numbers

print(average([1, 2, 3, 4, 5]))   # calling the function 'average'


print("\n")  # new line in the terminal

"""
Exercise 8:
Check If a Number is Positive or Negative: Write a function called check_number that takes a number and prints
whether the number is positive, negative, or zero.

Example:
check_number(10)  # Output: Positive
check_number(-5)  # Output: Negative
check_number(0)   # Output: Zero
"""

def check_number(number):      # define the function check_number that takes one parameter 'number'
    if number > 0:             # if the number is greater than zero display 'Positive'
        print("Positive")
    elif number < 0:           # if the number is less than zero display 'Negative'
        print("Negative")
    elif number == 0:          # if the number is equal to zero display 'Zero'
        print("Zero")

check_number(1234456)   # calling the function check_number when the parameter is greater than zero
check_number(- 876)     # calling the function check_number when the parameter is less than zero
check_number(0)         # calling the function check_number when the parameter is equal zero


print("\n")  # new line in the terminal

"""
Exercise 9:
Maximum of Three Numbers: Write a function find_max that takes three numbers as arguments and returns the
largest number.
"""

def find_max(number_1, number_2, number_3):    # define the function find_max that takes 3 arguments
    return max(number_1, number_2, number_3)   # returns the largest number of the 3 arguments

print(find_max(3423, 676786, 14879076))  # calling the function find_max


print("\n")  # new line in the terminal

"""
Exercise 10:
Area of a Circle: Write a function circle_area that takes the radius of a circle as an argument and returns the
area. Use the formula:
 Area= pi * r^2
 Use pi = 3.14.
"""
def circle_area(rad):     # define the function circle_area that calculates the area of a circle
    pi = 3.14
    area = pi * float(rad^2)    # formula for area of a circle
    return f"The area of a circle with the radius {rad} is: {area}"  # displays the area of a circle

print(circle_area(34))  # calling the function circle_area


print("\n")  # new line in the terminal

"""
Exercise 11:
Simple Calculator: Write a function calculator that takes three arguments: two numbers and an operator
(+, -, *, /). Perform the operation on the two numbers and return the result. Use a default operator of +.
"""

def calculator(number_1, number_2, operator="+"):   # define the function 'calculator' that takes 2 numerical
                                                    # arguments and 1 default operator ('+')
    if operator == "+":                  # if the operator is '+' calculates the sum of the 2 numbers
        return number_1 + number_2
    elif operator == "-":                # if the operator is '-' calculates the subtraction of the 2 numbers
        return number_1 - number_2
    elif operator == "*":                # if the operator is '*' calculates the multiplication of the 2 numbers
        return number_1 * number_2
    elif operator == "/":                # if the operator is '/' calculates the division of the 2 numbers
        return number_1 / number_2

print(calculator(3, 5))      # calling the function 'calculator' that takes the default operator '+'
print(calculator(6, 8, "-"))   # calling the function when the operator == '-'
print(calculator(9, 3, "*"))   # calling the function when the operator == '*'
print(calculator(4, 8, "/"))   # calling the function when the operator == '/'


print("\n")  # new line in the terminal

"""
Exercise 12:
Factorial Function: Write a function factorial that calculates the factorial of a number using a loop.
"""

def factorial(number):   # define the function 'factorial' that takes as a parameter a number and
                         # calculates its factorial
    fact = 1             # the variable 'fact' is created and initialized to 1
    for i in range(1, number + 1):   # a 'for' loop is used to calculate the factorial of 'number'
        fact *= i                    # in each iteration it multiplies 'fact' by the respective value of 'i'
    print(f"{fact} is the factorial for number {number}")  # it displays the factorial of 'number'

factorial(5)  # calling the function 'factorial'


print("\n")  # new line in the terminal

"""
Exercise 13:
List of Squares: Write a function list_of_squares that takes an integer n and returns a list containing the
squares of all numbers from 1 to n.

Example:

list_of_squares(5) -> [1, 4, 9, 16, 25]
"""

def list_of_squares(n):      # define the function 'list_of_squares'
    return [number ** 2 for number in range(1, n + 1)]   # the function returns a list containing the squares
                                                         # of all numbers from 1 to n

print(list_of_squares(5))  # calling the function 'list_of_squares'


print("\n")  # new line in the terminal

"""
Exercise 14:
Fibonacci Sequence: Write a function fibonacci that takes an integer n and prints the first n numbers in the
Fibonacci sequence.
"""

def fibonacci(n):   # define the function 'fibonacci' that takes one argument (n)
    sequence = [0, 1]   # initialize a list with the first 2 Fibonacci numbers
    for i in range(2, n):  # start a 'for' loop from index '2' to 'n-1'
        sequence.append(sequence[-1] + sequence[-2])  # calculate the next Fibonacci number by adding the last 2
                                                      # numbers in the sequence and appends the result to the end
                                                      # of the list
    return sequence[:n]       # returns the first 'n' elements of the list (it is sliced in case n is less than
                              # 2, so it doesn't return more than requested)

print(fibonacci(5))   # calling the function 'fibonacci'


print("\n")  # new line in the terminal

"""
Exercise 15:
Palindrome Checker: Write a function is_palindrome that checks whether a given string is a palindrome
(reads the same backward and forward).
"""

def is_palindrome(string):  # define the function 'is_palindrome' that takes a parameter 'string'
    string = string.lower().replace(" ", "")   # transforms all the letters in the string in lowercases and
                                               # removes the empy spaces
    return string == string[::-1]   # returns True if the elements are the same (a palindrome), or False if the
                                    # elements are different

print(is_palindrome("race car"))  # first call of the function 'is_palindrome', in this case the string is a palindrome
print(is_palindrome("curiosity")) # second call of the function 'is_palindrome', in this case the string
                                  # is not a palindrome


print("\n")  # new line in the terminal

"""
Exercise 16:
Prime Number Checker: Write a function is_prime that checks whether a number is prime.
"""

def is_prime(number):  # define the function 'is_prime' that takes 'number' as an argument
    if number % 2 == 0:   # checks if the number is prime
        print(f"Number {number} is a prime number.")  # display the following message is the number is prime
    else:
        print(f"Number {number} is not a prime number.") # display the following message is the number is not prime

is_prime(2)   # first call of the function 'is_prime', when the number is prime
is_prime(377) # second call of the function 'is_prime', when the number is not prime


print("\n")  # new line in the terminal

"""
Exercise 17:
Count Occurrences: Write a function count_occurrences that takes a list and a value as arguments and returns
the number of times the value appears in the list.
"""

def count_occurrences(a_list, a_value):  # define the function 'count_occurrences' that takes 2 arguments
    return a_list.count(a_value)     # the 'count' function is used to check the occurrences of 'a_value' in 'a_list'

list_1 = [1, 4, 7, 3, 4, 9, 2, 4, 5, 6, 8, 4]  # the variable 'list_1' is created and is given a list as a value
print(count_occurrences(list_1, 4))    # calling the function 'count_occurrences' with the arguments
                                              # a_list = list_1 and  a_value = 4


print("\n")  # new line in the terminal

"""
Exercise 18:
Password Strength Validator: Write a function validate_password that takes a password string and checks 
the following:

At least 8 characters long
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one number
The function should return True if the password is strong and False otherwise.
"""

def validate_password(password):  # define the function 'validate_password' that takes 1 argument (password)
    if (len(password) >= 8 and    # checks if the password length is greater or equal to 8
            any(character.isupper() for character in password) and  # checks if any character of the password is
                                                                    # an uppercase letter
            any(character.islower() for character in password) and  # checks if any character of the password is
                                                                    # a lowercase letter
            any(character.isdigit() for character in password)):    # checks if any character of the password is
                                                                    # a digit
        return True   # if the above conditions are met the function 'validate_password' returns True
    else:
        return False  # if the above conditions are not met the function 'validate_password' returns False

print(validate_password("password9")) # first call of the function, when the conditions are not met
print(validate_password("Password9")) # second call of the function, when the conditions are met


print("\n")  # new line in the terminal

"""
Exercise 19:
Simple Text Analyzer: Write a function text_analyzer that takes a string and returns the following:

Number of words
Number of characters (excluding spaces)
Number of vowels

Example:
text_analyzer("Hello World!")
-> Words: 2, Characters: 10, Vowels: 3
"""

def text_analyzer(a_string):   # define the function 'text_analyzer' that takes 1 argument (a_string)
    words = len(a_string.split())   # the variable 'words' is created and has the value 'len(a_string.split())'.
                                    # The functions 'len()' and 'split()' are used to count the number of words
    characters = len(a_string.replace(" ", ""))  # the variable 'words' is created and has the value
                                                 # 'len(a_string.replace(" ", ""))'. The functions 'len()' and
                                                 # 'replace()' are used to count the number of characters
    vowels = "aeiouAEIOU"    # the variable 'vowels' is created and is given as a value a string that contains
                             # all vowels
    vowels_count = sum(1 for character in a_string if character in vowels)  # the variable 'vowels_count' is created
                                                                        # and it value calculates the number of vowels
    return (f"The number of words is: {words} \n"      # returns the number of words in 'a_string'
            f"The number of characters is: {characters} \n" # returns the number of characters in 'a_string'
            f"The number of vowels: {vowels_count}") # returns the number of vowels in 'a_string'

print(text_analyzer("This is a string"))  # calling the function 'text_analyzer'


print("\n")  # new line in the terminal

"""
Exercise 20:
Temperature Converter: Write a function convert_temperature that converts temperature between Celsius and
Fahrenheit. Use the formulas:

Celsius to Fahrenheit: F=C×9/5+32
Fahrenheit to Celsius: C=(F−32)×5/9
"""

def convert_temperature(C, F):    # define function 'convert_temperature' that takes 2 arguments (C, F)
    temp_F = C * 9 / 5 + 32   # the variable 'temp_F' was created and its value is the formula to convert
                              # Celsius to Fahrenheit
    temp_C = (F - 32) * 5 / 9 # the variable 'temp_C' was created and its value is the formula to convert
                              # Fahrenheit to Celsius
    # the function returns the conversions: 'Celsius to Fahrenheit' and 'Fahrenheit to Celsius'
    return (f"{C} degrees Celsius were converted to {temp_F} degrees Fahrenheit. \n"
            f"{F} degrees Fahrenheit were converted to {temp_C} degrees Celsius.")

print(convert_temperature(10, 42))   # calling the function 'convert_temperature'


print("\n")  # new line in the terminal

"""
Exercise 21:
Create a Multiplication Table: Write a function multiplication_table that takes a number as input and prints
its multiplication table up to 10.
"""

def multiplication_table():   # define the function 'multiplication_table'
    number = int(input("Type a number: "))   # the variable 'number' is created and its value is an input from the user
    for i in range(1, 11):     # a for loop is used to display the multiplication table
        print(f"{number}x{i} = {number * i}")   # display the multiplication of the input with each number in the range

multiplication_table()   # calling the function 'multiplication_table'


print("\n")  # new line in the terminal

"""
Exercise 22:
Library: Create a class Book with the attributes title, author, year (publication year) and checked_out
(status indicating whether it is borrowed or not).
Create the following methods for this class:
- 2 methods to manage the loans: check_out(), return_book()
- 3 methods to compare the books: ==, <, > taking into account the book's title and author. It shall return
True or False
- a method to return the books info: book_info()
"""

class Book:  # define the class 'Book'
    def __init__(self, title, author, year):  # declare the atributts of the class
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False

    def check_out(self):   # define the method 'check_out' that checks if a book was borrowed or not
        if self.is_checked_out:
            print(f"The book {self.title} is not checked out")
        else:
            self.is_checked_out = True
            print(f"The book {self.title} has been checked out")

    def return_book(self):  # define the method 'return book' that checks if a book was returned or not
        if not self.is_checked_out:
            print(f"The book {self.title} is not checked out")
        else:
            self.is_checked_out = False
            print(f"The book {self.title} has been returned")

    def book_info(self):  # define the method 'book_info' that displays the book details and checked out status
        checked_out_status = "Yes" if self.is_checked_out else "No"
        print(f"Title: {self.title} \nAuthor: {self.author} \nYear: {self.year} \n"
              f"Checked out: {checked_out_status}")

    def __eq__(self, other):    # define the method '__eq__' that checks if a copy of a book exists based on
                                # author, title and release year
        return (self.title.lower() == other.title.lower() and
                self.author.lower() == other.author.lower() and
                self.year == other.year)

    def __lt__(self, other):   # define the method '__lt__' that checks which is the older book
        if self.title.lower() != other.title.lower():
            return self.title.lower() < other.title.lower()
        elif self.author.lower() != other.author.lower():
            return self.author.lower() < other.author.lower()
        else:
            return self.year < other.year

    def __gt__(self, other):    # define the method '__gt__' that checks which is the latest book
        if self.title.lower() != other.title.lower():
            return self.title.lower() > other.title.lower()
        elif self.author.lower() != other.author.lower():
            return self.author.lower() > other.author.lower()
        else:
            return self.year > other.year

    def __str__(self):    # define the 'str' method which displays the book details
        return f"'{self.title}' by {self.author} ({self.year})"

# below is the usage of the above class

book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
book1.book_info()

book1.check_out()
book1.check_out()

book1.book_info()

book1.return_book()
book1.return_book()
book1.book_info()

# print(book1)
# print book, compare books : ==, <, >
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
print(book1 > book2)

book1 = Book("Why we Sleep: Unlocking the Power od Sleep and Dreams", "Matthew Walker", 2017)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("1984", "Aldous Huxley", 1932)
book4 = Book("1984", "George Orwell", 1950)
print(book1 > book2)
print(book2 < book3)
print(book4 == book1)

library = [book2, book3, book4, book1]
sorted_library = sorted(library, reverse=True)
for book in sorted_library:
    print(book)


