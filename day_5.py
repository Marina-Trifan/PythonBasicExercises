"""
Exercise 1: Create a Class
Write a Python program that:
- creates a class called Person with attributes 'name' and 'age'
- includes a method 'introduce()' that prints: "Hello, my name is <name>, and I am <age> years old."
- create an object of the class and call the introduce() method.
"""

class Person:    # define the class 'Person'
    def __init__(self, name, age):   # declare the attributes of the class (name and age)
        self.name = name
        self.age = age

    def introduce(self):    # create the method 'introduce()' that displays the required text
        print(f"Hello, my name is {self.name}, and I am {self.age} years old.")


person = Person("John Snow", 24)   # create an object of class 'Person'
person.introduce()   # call the method 'introduce()'


print("\n")  # new line in the terminal

"""
Exercise 2: Class with Class and Instance Variables
Write a Python program that:
- creates class 'Book' with class variable 'total_books' initialized to 0
- each time a Book object is created, increment 'total_books'
- add attributes title and author to the class
- create three Book objects and print the total number of books created
"""

class Book:   # define the class 'Book'
    total_books = 0  # declare the class variable 'total_books' initialized to 0

    def __init__(self, title, author):   # declare class attributes (title and author)
        self.title = title
        self.author = author
        Book.total_books += 1    # for each book added updates 'total_books'

book_1 = Book("House of Flame and Shadow", "Sarah J. Mass")  # first class object
book_2 = Book("You Like It Darker", "Stephen King")          # second class object
book_3 = Book("The Anxious Generation", "Jonathan Haidt")    # third class object
print(f"Total number of books created: {Book.total_books}")  # displays the total number of books created


print("\n")  # new line in the terminal

"""
Exercise 3: Inheritance Example
Write a Python program that:
- creates a base class 'Animal' with a method 'sound()' that prints: "This animal makes a sound."
- creates a derived class 'Dog' that overrides the 'sound()' method to print: "The dog barks."
- creates objects of both classes and call their 'sound()' methods.
"""


class Animal:   # create the base class 'Animal'
    def sound(self):    # created the method 'sound()', that displays the requested message
        print("This animal makes a sound.")


class Dog(Animal):   # create the child class 'Dog' which inherits the method 'sound()' from the parent class 'Animal'
    def sound(self):      # override the inherited method 'sound()' to display the requested message
        print("The dog barks.")


cat = Animal()  # object of the base class 'Animal'
cat.sound()     # calling the function 'sound()' from the 'Animal' class

dog = Dog()  # object of the child class 'Dog'
dog.sound()  # calling the function 'sound()' from the 'Dog' class


print("\n")  # new line in the terminal

"""
Exercise 4: Polymorphism with Methods
Write a Python program that:
- creates a base class 'Shape' with method 'area()' that returns 0
- creates two derived classes 'Rectangle' and 'Circle':
    - the 'Rectangle' class should override 'area()' to calculate the area as length * width
    - the 'Circle' class should override 'area()' to calculate the area as π * radius².
- creates objects of 'Rectangle' and 'Circle' and call their 'area()' methods.
"""

class Shape:    # create the base class 'Shape'
    def area(self):   # create the method 'area()' that returns 0
        return 0

class Rectangle(Shape):  # create the child class 'Rectangle' which inherits the parent class 'Shape'
    def __init__(self, length, width):  # declare the class attributes (length and width)
        self.length = length
        self.width = width

    def area(self):    # override the inherited method 'are()' which calculates the area of a rectangle
        return self.length * self.width

class Circle(Shape):   # create the child class 'Circle' which inherits the parent class 'Shape'
    def __init__(self, radius):
        self.radius = radius

    def area(self):   # override the inherited method 'are()' which calculates the area of a circle
        Pi = 3.14     # variable that takes the value of Pi
        return Pi * self.radius ** 2

rectangle = Rectangle(14, 6)   # object of the child class 'Rectangle'
print(f"The rectangle area is: {rectangle.area()}")  # calling the function 'area()' from the child class 'Rectangle'

circle = Circle(15)   # object of the child class 'Circle'
print(f"The circle area is: {circle.area()}")  # calling the function 'area()' from the child class 'Circle'


print("\n")  # new line in the terminal

"""
Exercise 5: Encapsulation Example
Write a Python program that:
- creates a class 'BankAccount' with private attributes '__account_number' and '__balance'
- includes methods to:
    - get the balance
    - deposit money
    - withdraw money (ensure the balance doesn't go negative)
- creates on object and demonstrate depositing and withdrawing money.
"""

class BankAccount:   # create the class 'BankAccount'
    def __init__(self, account_number, balance):   # declare class private attributes (__account_number and __balance)
        self.__account_number = account_number
        self.__balance = balance

    def get_the_balance(self):   # create 'get_the_balance' method, which displays the balance for a specific account
        print(f"The balance for the account number {self.__account_number} is: {self.__balance}")

    def deposit_money(self):   # create 'deposit_money' method
        deposit = int(input("Introduce the amount that you what to deposit: "))  # the user is asked to insert
                                                                                 # the amount to be deposited
        self.__balance += deposit   # the deposited amount is added to user's balance
        print(f"The amount {deposit} was introduced to your account."   # display the updated balance
              f" Your current balance is:{self.__balance}")

    def withdraw_money(self):   # create 'withdraw_money' method
        withdraw_amount = int(input("Introduce the amount that you want to withdraw: ")) # the user is asked to insert
                                                                                         # the amount to be withdrawn
        if self.__balance >= withdraw_amount:   # if user's balance is greater than or equal to the amount to
                                                # be withdrawn than:
            self.__balance -= withdraw_amount   # withdraw the requested amount
            print(f"The amount {withdraw_amount} was withdraw from your account."   # display the updated balance
                  f"Your current balance is:{self.__balance} ")
        else:     # if user's balance is insufficient for the withdrawal display the appropriate message
            print(f"Your balance {self.__balance} is insufficient for the withdrawal.")

account = BankAccount(123456, 450)  # the class 'BankAccount' object
account.get_the_balance()  # calling the method 'get_the_balance'
account.deposit_money()    # calling the method 'deposit_money'
account.withdraw_money()   # calling the method 'withdraw_money'


print("\n")  # new line in the terminal

"""
Exercise 6: Student Management System
Write a Python program that:
- creates a class 'Student' with attributes 'name', 'grade', and 'marks'
- includes methods to :
    - display the student's information
    - determinate if the student passed (marks >= 50)
- create a list of students and display the information for all students who passed.
"""

class Student:   # create class 'Student'
    def __init__(self, name, grade, marks):    # define class attributes (name, grade, marks)
        self.name = name
        self.grade = grade
        self.marks = marks

    def display_student_information(self):   # create the method 'display_student_information' which returns
                                             # a string containing the student information
        return f"Student information: Name = {self.name}, grade = {self.grade}, marks = {self.marks}"

    def passed(self):    # create the method 'passed' which determines if a student has passed
        return self.marks >= 50

# create a list of students:
list_of_students = [Student("J. K. Rowling", 9, 60),
                    Student("Dante Alighieri", 8, 70),
                    Student("Stephen King", 5, 45),
                    Student("Sarah J. Mass", 10, 90)]

# to display the students who passed a for loop is used:
for student in list_of_students:
    if student.passed():  # calling the method 'passed'
        print(student.display_student_information())  # displays the information only for the students that passed


print("\n")  # new line in the terminal

"""
Exercise 7: Tic-Tac-Toe Game Setup
Write a Python program that:
- creates a class 'TicTacToe' with:
    - an attribute 'board' to store the 3x3 grid as a list of lists
    - a method 'display_board()' to print the grid
    - a method 'make_move(row, col, player)' to update the grid
- create an object and make a few moves to test the setup.
"""

class TicTacToe:   # create the class 'TicTacToe'
    def __init__(self):
        self.board = [    # class attribute that stores a 3x3 grid as a list of lists
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def display_board(self):    # create the method 'display_board' that prints the grid
        for row in self.board:
            print(row)
        print(15 * "-")   # display a line of '-' to delimit the grids after each move

    def make_move(self, row, col, player):    # create the method 'make_move'
        if row < 3 and col < 3 and row >= 0 and col >= 0:
            if self.board[row][col] == " ":
                self.board[row][col] = player
                self.display_board()
            else:
                print("A move has been done on that spot.")
        else:
            print("Not on board")
            print(15 * "-")  # display a line of '-' to delimit the messages that represents the wrong moves

game1 = TicTacToe()
game1.make_move(0, 2, "x")
game1.make_move(0, 1, "0")
game1.make_move(0, 2, "0")
game1.make_move(0, 5, "X")
game1.make_move(1, -2, "0")


print("\n")  # new line in the terminal

"""
Exercise 8:

Write a Python program that:
- creates a class which can store all the information related to a magical creature
- create a list of objects (every objects must be a creature from the dictionary.
Use below dictionary:
fantasy_creatures = {
    "Phoenix": {
        "habitat": "Volcanic mountains",
        "abilities": {
            "rebirth_from_ashes": "Can regenerate itself by rising from its own ashes",
            "healing_tears": "Tears have the power to heal wounds and ailments",
            "fire_manipulation": "Can control and generate flames"
        },
        "diet": ["Ash", "Magical herbs", "Carrion"],
        "rarity": "Legendary",
        "lifespan_years": 500,
        "is_endangered": True
    },
    "Griffin": {
        "habitat": "High cliffs and mountain ranges",
        "abilities": {
            "sharp_talons": "Powerful claws used for hunting and defense",
            "flight": "Can soar at great heights and speeds",
            "keen_eyesight": "Exceptional vision for spotting prey from afar"
        },
        "diet": ["Carrion", "Small mammals", "Birds"],
        "rarity": "Rare",
        "lifespan_years": 150,
        "is_endangered": False
    },
    "Dragon": {
        "habitat": "Caverns and hidden valleys",
        "abilities": {
            "fire_breathing": "Expels a stream of fire from its mouth",
            "immense_strength": "Possesses incredible physical power",
            "flight": "Has large wings enabling long-distance flight"
        },
        "diet": ["Livestock", "Jewels", "Precious metals"],
        "rarity": "Legendary",
        "lifespan_years": 1000,
        "is_endangered": False
    }
}
"""
fantasy_creatures = {
    "Phoenix": {
        "habitat": "Volcanic mountains",
        "abilities": {
            "rebirth_from_ashes": "Can regenerate itself by rising from its own ashes",
            "healing_tears": "Tears have the power to heal wounds and ailments",
            "fire_manipulation": "Can control and generate flames"
        },
        "diet": ["Ash", "Magical herbs", "Carrion"],
        "rarity": "Legendary",
        "lifespan_years": 500,
        "is_endangered": True
    },
    "Griffin": {
        "habitat": "High cliffs and mountain ranges",
        "abilities": {
            "sharp_talons": "Powerful claws used for hunting and defense",
            "flight": "Can soar at great heights and speeds",
            "keen_eyesight": "Exceptional vision for spotting prey from afar"
        },
        "diet": ["Carrion", "Small mammals", "Birds"],
        "rarity": "Rare",
        "lifespan_years": 150,
        "is_endangered": False
    },
    "Dragon": {
        "habitat": "Caverns and hidden valleys",
        "abilities": {
            "fire_breathing": "Expels a stream of fire from its mouth",
            "immense_strength": "Possesses incredible physical power",
            "flight": "Has large wings enabling long-distance flight"
        },
        "diet": ["Livestock", "Jewels", "Precious metals"],
        "rarity": "Legendary",
        "lifespan_years": 1000,
        "is_endangered": False
    }
}

class MagicalCreaturesInformation:   # create class 'MagicalCreatureInformation'
    # create class attributes (name, habitat, abilities, diet, rarity, lifespan_years, is_endangered)
    def __init__(self, name, habitat, abilities, diet, rarity, lifespan_years, is_endangered):
        self.name = name
        self.habitat = habitat
        self.abilities = abilities
        self.diet = diet
        self.rarity = rarity
        self.lifespan_years = lifespan_years
        self.is_endangered = is_endangered

    def __str__(self):   # create method '__str__' to display creature information
        return (f"Magical creature {self.name}, habitat: {self.habitat}, abilities: {self.abilities}, "
                f"diet: {self.diet}, rarity: {self.rarity}, lifespan in years: {self.lifespan_years},"
                f"is endangered: {self.is_endangered}")

list_of_magical_creatures = []  # create an empty list that will store magical creatures information
for name, data in fantasy_creatures.items():  # using a 'for' loop to access creature information from the dictionary
    print(f"Name = {name}")
    print(f"Data = {data}")
    creature = MagicalCreaturesInformation(   # create class objects
        name=name,
        habitat=data["habitat"],
        abilities=data["abilities"],
        diet=data["diet"],
        rarity=data["rarity"],
        lifespan_years=data["lifespan_years"],
        is_endangered=data["is_endangered"]
    )

    list_of_magical_creatures.append(creature)  # append the empty list with the objects created


print("\n")  # new line in the terminal

"""
Exercises: Python Basics - Recap
1.Declare two variables, x and y, with values 5 and 10. Swap their values and print them.
2.Write a Python program to calculate the area of a rectangle (length × width).
3. Print the data type of the following variables:
a = 42
b = 3.14
c = "Hello"
d = True
"""
# 1
x = 5   # declare variable 'x' that takes the value 5
y = 10  # declare variable 'y' that takes the value 10
x, y = y, x   # swap the values of the 2 variables
print(f"After swapping: x = {x}, y = {y}.")   # display the value of variables 'x' and 'y' after swapping

# 2

# first option:
rectangle_length = 456   # declare the variable 'rectangle_length' with the value 456
rectangle_width = 123    # declare the variable 'rectangle_length' with the value 456
rectangle_area = rectangle_length * rectangle_width  # declare variable 'rectangle_area',
                                                     # its value calculates the area of the rectangle
print(f"The area of the rectangle with the length {rectangle_length} and width {rectangle_width} is: "
      f"{rectangle_area}")   # displays the area of the rectangle

# second option:
def calculate_rectangle_area(length, width):  # define the function 'calculate_rectangle_area' with 2 attributes
                                              # length and width
    rectangle_area = length * width  # declare the variable 'rectangle_area' which value calculates the area of
                                     # a rectangle using function attributes
    # display the rectangle area:
    print(f"The area of the rectangle with the length {length} and width {width} is: {rectangle_area}")

calculate_rectangle_area(101, 99)  # calling the function 'calculate_rectangle_area'

# 3
a = 42
b = 3.14
c = "Hello"
d = True

print(type(a))  # displays the type of variable 'a'
print(type(b))  # displays the type of variable 'b'
print(type(c))  # displays the type of variable 'c'
print(type(d))  # displays the type of variable 'd'

print("\n")  # new line in the terminal

"""
Exercises: Operators and Operations
1.	Write a program to check if a number is divisible by both 3 and 5.
2.	Given two numbers, calculate and print the result of all arithmetic operations (addition, subtraction,
multiplication, etc.).
3.	Write a Python program that takes three numbers as input and prints the largest among them.
"""
# 1
def number_divisibility(number):   # create the function 'number_divisibility' which takes one argument (number)
    if number % 3 == 0 and number % 5 == 0:  # if 'number' is divisible both, by 3 and 5 display the below message
        print(f"Number {number} is divisible by 3 and 5")
    elif number % 3 == 0:   # if 'number' is divisible ony by 3 display the below message
        print(f"Number {number} is only divisible by 3")
    elif number % 5 == 0:   # if 'number' is divisible ony by 5 display the below message
        print(f"Number {number} is divisible only by 5")
    else:    # if any of the conditions above is not met display the below message
        print(f"Number {number} isn't divisible either by 3, or 5")

number_divisibility(5)  # calling the function 'number_divisibility' when 'number' is divisible only by 5
number_divisibility(15) # calling the function 'number_divisibility' when 'number' is divisible by 3 and 5
number_divisibility(9)  # calling the function 'number_divisibility' when 'number' is divisible only by 2
number_divisibility(22) # calling the function 'number_divisibility' when 'number' isn't divisible by 3, or 5

# 2
def math_operations(number_1, number_2):  # define the function 'math_operations' with 2 arguments (number_1, number_2)
    addition = number_1 + number_2  # declare a variable 'addition', which value adds the 2 arguments
    print(f"The addition of first number to second number is: {addition}") # displays the result of 'addition'

    subtraction = number_1 - number_2 # declare a variable 'subtraction', which value subtracts the 2 arguments
    print(f"The subtraction of second number from first number is: {subtraction}") # displays the result of 'subtraction'

    product = number_1 * number_2 # declare a variable 'product', which value multiplies the 2 arguments
    print(f"The multiplication of first number with second number is: {product}") # displays the result of 'product'

    if number_2 != 0:  # checks if 'number_2' is different from zero
        division = number_1 / number_2 # if 'number_2' is different fom zero calculate the division of the 2 arguments
        print(f"The result of first number divided by second number is: {division}") # displays the result of 'division'
    else:  # when 'number_2' is zero the division of the 2 arguments is not calculated
        print("Division by zero isn't possible")  # instead of dividing the 2 arguments, this message is displayed

    power = number_1 ** number_2 # declare a variable 'power', which value calculates
                                 # 'number_1' to the power of 'number_2
    print(f"The result of first number to the power of second number is: {power}") # displays the result of 'power'

    if number_2 != 0:  # checks if 'number_2' is different from zero
        division_integer = number_1 // number_2 # if 'number_2' is different fom zero calculate the
                                                # integer of the division
        print(f"The integer of the division of first number to second number is: {division_integer}") # displays
                                                                                                    # 'division_integer'
    else:  # when 'number_2' is zero the integer of the division of the 2 arguments is not calculated
        print("Division by zero isn't possible") # instead of dividing the 2 arguments, this message is displayed

    if number_2 != 0: # checks if 'number_2' is different from zero
        remainin_of_the_division = number_1 % number_2 # if 'number_2' is different fom zero calculate the
                                                       # remaining of the division of the 2 arguments
        # displays the remaining of the division:
        print(f"The remaining of the division of first number to second number is: {remainin_of_the_division}")
    else: # when 'number_2' is zero the remaining of the division is not calculated
        print("Division by zero isn't possible") # instead of dividing the 2 arguments, this message is displayed


math_operations(3, 5)   # first call of the function, when 'number_2' isn't zero
print(100 * "-")  # delimits the 2 calls of the function
math_operations(60, 0)  # second call of the function, when 'number_2' is zero

# 3
number_1 = int(input("Type the first number: "))  # declare variable 'number_1' which value is an input from the user
number_2 = int(input("Type the second number: ")) # declare variable 'number_2' which value is an input from the user
number_3 = int(input("Type the third number: ")) # declare variable 'number_3' which value is an input from the user
largest_number = [number_1,number_2, number_3] # declare variable 'largest_number' which value is a list of the 3 numbers
print(f"The largest number of the 3 inputs is: {max(largest_number)}") # display the largest number of the 3 inputs
                                                                       # using the max function on the list of numbers

print("\n")  # new line in the terminal

"""
Exercises: Strings
1.	Write a program that alternates the case of letters in a string. For example, "hello" becomes "HeLlO"..
2.	Write a program that takes a sentence as input and prints the longest word in the sentence.
3.	Write a program that checks if two strings entered by the user are anagrams (contain the same characters
in a different order).
"""
# 1

# declare the variable 'a_string' that has a string as value
a_string = "Any sufficiently advanced technology is indistinguishable from magic."

alternated_characters = ""  # declare an empty variable
for index, character in enumerate(a_string): # using the 'for' loop to access each character in 'a_string' by index
      if index % 2 == 0:  # checks if the index is divisible by 2
            alternated_characters += character.upper() # add to 'alternated_characters' the characters that have
                                                       # the index divisible by 2 and change these characters to
                                                       # uppercase letters
      else:
          # when the remaining of the division is different from 0, add to 'alternated_characters' the respective
          # characters and change these characters to lowercase letters
            alternated_characters += character.lower()
print(f"Alternated characters in a_string: {alternated_characters}") # displays the string with alternated characters

# 2
a_sentence = input("Write a sentence: ")  # declare the variable 'a_sentence', which value is an input from the user
words = a_sentence.split() # declare the variable 'words' which value is a list of the words from 'a_sentence'
longest_word = ""  # declare the variable 'longest_word' initialized as an empty string
max_length = 0     # declare the variable 'max_length' initialized to 0
for word in words: # a 'for' loop is used to access each individual item (word) from the list (words)
      if len(word) > max_length:  # checks if the length of the word is greater than the variable 'max_length'
            max_length = len(word) # if the above condition is met, 'max_length' takes as a value 'len(word)'
            longest_word = word # if the above condition is met, 'longest_word' takes as a value 'word'
print(f"The longest word in a_sentence is: {longest_word}") # displays the longest word from 'a_sentence'

# 3

# declare the variables 'string_1' and 'string_2' which values are an input from the user. In case the input is a
# sentence, the empty spaces are eliminated by using the 'replace()' function, and because Python differentiate
# uppercases from lowercases the 'lower()' function is used to transform all characters to lowercase
string_1 = input("Write the first string: ").replace(" ", "").lower()
string_2 = input("Write the second string: ").replace(" ", "").lower()

if sorted(string_2) == sorted(string_1): # the 'sorted()' function is used to check if both strings have the
                                         # same characters
      print("The second string is an anagram of the first string") # displays the message only if both strings
                                                                   # contain the same characters
else:
      print("The second string is not an anagram of the first string") # displays the message only if the strings
                                                                   # don't contain the same characters


print("\n")  # new line in the terminal

"""
Exercises: Lists, Dictionaries, Tuples, and Sets
1.	Create a list of numbers and find their sum and average.
2.	Create a dictionary to store the names and grades of 5 students. Print the name of the student with the
highest grade.
3.	Convert a tuple (1, 2, 3, 4) into a list and add the number 5.
"""
# 1
list_of_numbers = [3, 6, 3, 2, 7, 85, 4, -54] # declare the variable 'list_of_numbers', its value is a list of numbers
sum_of_numbers = sum(list_of_numbers) # declare the variable 'sum_of_numbers', its value is the sum of
                                      # numbers from 'list_of_numbers' using the 'sum()' function
average_of_numbers = sum_of_numbers/(len(list_of_numbers)) # declare the variable 'average_of_numbers',
                                                           # that stores the average of the numbers from 'list_of_numbers'
print(f"The sum of numbers from list_of_numbers is: {sum_of_numbers}") # displays the sum of numbers from 'list_of_numbers'
print(f"The average of numbers from list_of_numbers is: {average_of_numbers}") # displays the average of numbers from
                                                                               # 'list_of_numbers'
# 2
students_dictionary = {  # create the dictionary 'students_dictionary', that stores the names and grades of 5 students
      "Student 1": {     # first item of the dictionary, which stores in another dictionary the name and grade
                         # of the first student
            "name": "Sonja Henie",
            "grade": 9
      },
      "Student 2": {     # second item of the dictionary, which stores in another dictionary the name and grade
                         # of the second student
            "name": "Dick Button",
            "grade": 7
      },
      "Student 3": {     # third item of the dictionary, which stores in another dictionary the name and grade
                         # of the third student
            "name": "Peggy Fleming",
            "grade": 5
      },
      "Student 4": {     # forth item of the dictionary, which stores in another dictionary the name and grade
                         # of the forth student
            "name": "Dorothy Hamill",
            "grade": 8
      },
      "Student 5": {     # fifth item of the dictionary, which stores in another dictionary the name and grade
                         # of the fifth student
            "name": "Kristi Yamaguchi",
            "grade": 6
      },
}
student_name = None # create a variable 'student_name', initially set to 'None'
student_grade = float("-inf") # create a variable 'highest_grade', initially set to negative infinity using 'float("-inf")'
for student, info in students_dictionary.items():  # a 'for' loop is used to access the items of the dictionary
      if info["grade"] > student_grade:  # checks if the grade of a student is greater than the variable 'student_grade'
            student_grade = info["grade"]  # the variable 'highest_grade' will store the highest grade
            student_name = info["name"] # the variable 'student_name' will store the name of the student with the highest grade
print(f"Student {student_name} has the highest grade: {student_grade}") # displays the name and grade of the student
                                                                        # with the highest grade

# 3
a_tuple = (1, 2, 3, 4) # declare a tuple
tuple_converted_to_list = list(a_tuple) # converts 'a_tuple' to a list using the 'list()' function
print(type(tuple_converted_to_list))    # displays the type of 'tuple_converted_to_list' using the 'type()' function
tuple_converted_to_list.append(5)       # adds number 5 to the list (tuple_converted_to_list)
print(tuple_converted_to_list)          # displays updated list (tuple_converted_to_list)


print("\n")  # new line in the terminal

"""
Exercises: Conditional Statements
1.	Leap Year Checker: Write a program to determine if a given year is a leap year. A year is a leap year if:
    - It is divisible by 4, but not divisible by 100, or
    - It is divisible by 400.
2.	Write a program that asks the user to enter their age and prints:
    - "Child" if the age is less than 13.
    - "Teen" if the age is between 13 and 19.
    - "Adult" otherwise.
3.	Write a program that asks the user to input a number (1–7) and prints the corresponding day of the week.
For example:
            1: "Monday"
            2: "Tuesday"
            ...
            7: "Sunday"
    - Print "Invalid input" for any number outside the range 1–7.
"""
# 1
year = int(input("Write your year: ")) # declare variable 'year',
                                       # which value is an integer (int()) from the user (input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: # checks if 'year' is divisible by 4 or 400,
                                                         # and not divisible by 100
      print(f"{year} is a leap year")  # when 'year' meets the above condition display this message
else:
      print(f"{year} is not a leap year") # when 'year' doesn't meet the above condition display this message

# 2
user_age = int(input("Write your age: ")) # declare variable 'user_age',
                                          # which value is a user input representing its age
if user_age < 13:   # checks if the user's age is smaller than 13
      print("Child")  # when the user's age is smaller than 13, display 'Child'
elif user_age >= 13 and user_age < 19: # checks if user's age is between 13 and 19
      print("Teen")  # when user's age is between 13 and 19 display 'Teen'
else:
      print("Adult")  # if none of the above condition are met display 'Adult'

# 3
number = int(input("Write a number between 1 and 7: ")) # declare variable 'number',
                                                        # which value asks (input) the user for a number between 1 and 7
if number == 1:  # checks if the number is 1
      print("Monday") # when the number is 1 display this message
elif number == 2:  # checks if the number is 2
      print("Tuesday") # when the number is 2 display this message
elif number == 3:  # checks if the number is 3
      print("Wednesday") # when the number is 3 display this message
elif number == 4:  # checks if the number is 4
      print("Thursday") # when the number is 4 display this message
elif number == 5:  # checks if the number is 5
      print("Friday") # when the number is 5 display this message
elif number == 6:  # checks if the number is 6
      print("Saturday") # when the number is 6 display this message
elif number == 7:  # checks if the number is 7
      print("Sunday") # when the number is 7 display this message
else:  # if the user's input is not a number between 1 and 7 display the below message
      print("Incorrect input")


print("\n")  # new line in the terminal

"""
Exercises: Loops (While and For)
1.	Write a program that calculates the sum of all even numbers from a list.
2.	Write a program to count how many times the letter "a" appears in a string entered by the user.
(using for/while).
3.	Write a program that calculates the sum of the digits of a number entered by the user. For example, if the
input is 1234, the output should be 10.
4.	Write a program that takes a series of numbers entered by the user (ending with -1 to stop) and prints the
largest number entered.
"""
# 1
list_of_numbers = [1, 3, 4, 778, 242, 778, 32, 78, 11, 67, 0] # declare variable 'list_of_numbers',
                                                              # which value is a list of numbers

even_numbers = [] # declare variable 'even_numbers', which is initialized with an empty list
for number in list_of_numbers:  # a 'for' loop is used to go through each number from 'list_of_numbers' individually
      if number % 2 == 0:  # checks each number if it is an even number
            even_numbers.append(number)  # when a number is even it adds it to the list 'even_numbers'
            even_numbers_sum = sum(even_numbers)  # declare variable 'even_numbers_sum',
                                                  # which value is calculating the sum of all even numbers
print(f"The sum of all even numbers from 'list_of_numbers'is: {even_numbers_sum}") # displays the sum of all even numbers

# 2
user_string = input("Write a sentence: ")

# option 1: without using loops
count_a = user_string.lower().count('a') # declare the variable 'count_a',
                                         # it's value transforms user's input into lowercases and counts how
                                         # many times 'a' appears in the string
print(f"Letter 'a' appears {count_a} times in the inputted string") # displays letter 'a' occurrences in the string


#option 2: using the 'for' loop
count_list = []  # declare the variable 'count_list' that is initialized as an empty list
for letter in user_string.lower(): # a 'for' loop is used to check each letter from the input
      if letter == "a":  # checks if a letter is 'a'
          count_list.append(letter)  # for each occurrence of 'a' in the string it appends the 'count_list' with an 'a'

counting_a = len(count_list)  # declare the variable 'counting_a', which calculates how many times 'a' appears
                              # in the input by using the 'len()' function
print(f"Letter 'a' appears {counting_a} times in the inputted string")

# 3
user_number = input("Write a number: ") # declare variable 'user_number', which value is a number from the user
list_of_digits = []   # declare variable 'list_of_digits', initialized as an empty list
for number in user_number:  # a 'for' loop is used to access each number from 'user_number'
      digit = int(number)   # since 'number' is considered a string the variable 'digit' was declared, and
                            # it's value transforms the number from string to integer using the 'int()' function
      list_of_digits.append(digit) # each digit is saved in 'list_of_digits'
print(f"The sum of the digits of a number entered by user is: {sum(list_of_digits)}")

# 4

# option 1:
largest_number = 0  # declare the variable 'largest_number' that is initialized to 0
while True: # a 'while' loop is used to check which number is the largest number
      number = int(input("Write a number and use -1 to stop: ")) # declare variable 'number',
                                                                 # which takes an input from the user as it's value
      if number == -1:  # checks if 'number' has the value -1
            break       # if the value of 'number' is -1 break the loop
      if number > largest_number:  # checks if 'number' is greater than 'largest_number'
            largest_number = number  # if condition is True 'largest_number' takes the value of 'number'
print(f"The largest number entered is: {largest_number}")  # displays the largest number entered by the user

# option 2:
numbers_list = [] # declare the variable 'numbers_list' that is initialized to an empty list
while True: # a 'while' loop is used to check which number is the largest number
      number = int(input("Write a number and use -1 to stop: ")) # declare variable 'number',
                                                                 # which takes an input from the user as it's value
      if number == -1:  # checks if 'number' has the value -1
            break       # if the value of 'number' is -1 break the loop
      else:  # if the above condition is not met add the number to 'numbers_list' using the 'append()' function
            numbers_list.append(number)
largest_number = max(numbers_list)  # declare the variable 'largest_number', which takes the largest number
                                    # from 'numbers_list' as its value, using the 'max()' function
print(f"The largest number entered is: {largest_number}")  # displays the largest number entered by the user

print("\n")  # new line in the terminal

"""
Exercises: Functions
1.	Write a function that takes a list of numbers as input and returns the largest number.
2.	Write a function find_unique that takes a list of numbers and returns a list of unique elements from it.
3.	Write a function count_vowels that takes a string and returns the number of vowels (a, e, i, o, u) in the
string.
"""
# 1
def find_largest_number():  # define the function 'find_largest_number'
    list_of_numbers = input("Write a list of numbers: ") # declare variable 'list_of_numbers',
                                                         # which takes a list of numbers from the user as its value
    return f" The largest number is: {max(list_of_numbers)}" # the function returns the largest number
                                                             # from the list using the 'max()' function

print(find_largest_number())  # display the largest number returned by the function 'find_largest_number'

# 2
def find_unique():   # define the function 'find_unique'
    list_of_numbers = [1, 3, 2, 4, 6, 7, 9, 3]  # declare the variable 'list_of_numbers', and its value is a list of numbers
    list_of_unique = list(set(list_of_numbers)) # declare the variable 'list_of_unique',
                                                # and its value is a list of unique numbers arranged in ascending order
    print(list_of_unique) # displays the list of unique numbers

find_unique() # calling the function 'find_unique'

# 3
def count_vowels():   # define the function 'count_vowels', which counts the number of vowels in a string
    a_string = input("Write a sentence: ")  # declare the variable 'a_string', that its value is an input from the user
    vowels = "aeiou"  # declare the variable 'vowels' and its value is a string of all vowels
    total_vowels = []  # declare the variable 'total_vowels' that is initialized to an empy list
    for letter in a_string.lower(): # a 'for' loop is used to check each letter from 'a_strig'. The 'lower()'
                                    # function is used to turn all letters in 'a_string' to lower case letters
        if letter in vowels:  # checks if any letter from 'a_string' is a vowel
            total_vowels.append(letter)  # if the above condition is met add the letter to 'total_vowels'
    print(f"The number of vowels in a_string is: {len(total_vowels)}") # displays the total number of vowels in 'a_string'

count_vowels()  # calling the function 'count_vowels'


print("\n")  # new line in the terminal

"""
Exercises: Object-Oriented Programming (Basic OOP)
1.	Write a Python program:
    - Create a class 'Movie' with attributes 'title', 'director', 'release_year', 'rating', and 'comments'.
    - Use a setter method to ensure that the rating is between 0 and 10.
    - Create methods to add a comment and retrieve all comments for a movie.
    - Implement a method to display the movie's details along with its rating and comments.
    - Demonstrate adding comments and changing ratings for a movie.
2. Write a Python program:
    - Create a class Person with the following attributes: 'name', 'age', and 'email'
    - Create a text file people.txt where each line contains data for a person. The data for each person will
be separated by commas. For example:
        John Doe,30,johndoe@example.com
        Jane Smith,25,janesmith@example.com
        Alice Brown,35,alicebrown@example.com
    - Read the people.txt file, process each line, and create a Person object for each line.
    - Store all created Person objects in a list.
    - After reading all lines from the file, display the details of each person by iterating through the list
of Person objects.

"""
# 1
class Movie:   # define class 'Movie'
    def __init__(self, title, director, release_year, rating, comments):  # create class arguments
        self.title = title
        self.director = director
        self.release_year = release_year
        self.rating = rating
        self.comments = comments
        self.all_comments = [self.comments] # create a list to store all comments for a movie

    def set_rating(self, rating):  # define the method 'set_rating', which ensures that te rating is between 0 and 1
        self.rating = max(0, min(10, rating))

    def add_comment(self, comment):  # define the method 'add_comment', which saves the added comment into 'self.all_comments'
        self.all_comments.append(comment)

    def retrieve_all_comments(self):  # define the method 'retrieve_all_comments, which returns all comments for a movie
        return f"All comments for movie '{self.title}' are: {self.all_comments}"

    def display_details(self):  # define method 'display_details', which displays all details for a movie
        print(f"Movie details: {self.title} - {self.director} ({self.release_year}) "
              f"rating: {self.rating}, comments: {self.comments}")


movie_1 = Movie("Zack Snyder's Justice League", "Zack Snyder",
                2021, 8, "first movie comment")  # object of class 'Movie'
movie_1.display_details()  # calling the method 'display_details()' for object 'movie_1'

movie_2 = Movie("Another Simple favor", "Paul Feig",
                2025, 5, "second movie comment") # object of class 'Movie'
movie_2.display_details()  # calling the method 'display_details()' for object 'movie_2'

movie_3 = Movie("The Boogeyman", "Rob Savage",
                2023, 6, "third movie comment")  # object of class 'Movie'
movie_3.display_details()  # calling the method 'display_details()' for object 'movie_3'

movie_1.add_comment("first movie second comment") # calling the method 'add_comment()' for object 'movie_1'
print(movie_1.retrieve_all_comments()) # calling the method 'retrieve_all_comments()' for object 'movie_1'
movie_1.display_details() # calling the method 'display_details()' for object 'movie_1', after adding another comment

movie_2.set_rating(7) # calling the method 'set_rating()' for object 'movie_2'
movie_2.display_details()# calling the method 'display_details()' for object 'movie_2', after changing the rating

# 2

class Person:  # define class 'Person'
    def __init__(self, name, age, email):  # create class attributes
        self.name = name
        self.age = age
        self.email = email


with open("people.txt", "w") as file:  # create the text file 'people'
    file.writelines("Robert De Niro, 82, robert@example.com\n")    # write in the text file
    file.writelines("Morgan Freeman, 88, morgan@example.com\n")    # write in the text file
    file.writelines("Julia Roberts, 58, julia@example.com\n")      # write in the text file
    file.writelines("Natalie Portman, 44, natalie@example.com\n")  # write in the text file

list_of_persons = [] # declare the variable 'list_of_persons' initialized to an empty list
with open("people.txt", "r") as file:  # read the text file created
    for line in file:  # a 'for' loop is used to go through each line of the file
        line = line.strip()  # removes any empty spaces from a line
        if line:  # skips the line if it is empty
            name, age, email = line.split(",") # extracts the variables 'name', 'age', 'email' from a line
                                               # and separates it by comma
            person = Person(name.strip(), age.strip(), email.strip())  # create object of class 'Person'
            list_of_persons.append(person)  # adds 'person' to 'list_of_persons'

for person in list_of_persons: # a 'for' loop is used to go through each person from 'list_of_persons'
    print(f"Name: {person.name}, Age: {person.age}, Email: {person.email}")  # displays the details of each person