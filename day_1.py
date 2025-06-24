"""
Exercise 1:
Create a variable name and assign your name to it as a string. Then print: "Hello, <your name>!" using
the f-string format.
"""
name = "Trifan Marina Valentina"
print(f"Hello, {name}")

print("\n")

"""
Exercise 2:
Write a Python program to calculate the area of a rectangle. Take length and width as variables and 
print the area in the format: "The area of the rectangle is <area>".
"""
length = 5
width = 4
area = length * width
print(f"The area of the rectangle is {area}")

print("\n")

"""
Exercise 3:
Create a variable number and assign it a number. Write a program that prints:
The number itself.
The square of the number.
The cube of the number. Format the output using f-strings
"""

number = 6
print(f"The number itself is: {number}. \n"
      f"The square of the number is: {number**2}. \n"
      f"The cube of the number is: {number**3}")

print("\n")

"""
Exercise 4:
Write a Python program that takes two numbers as inputs and swaps their values. For example:
If the first input is 5 and the second is 10, the program should print:
less
Copy the code:
Before swapping: a = 5, b = 10
After swapping: a = 10, b = 5
"""
number_1 = int(input("Type the first number: "))
number_2 = int(input("Type the second number: "))
print(f"Before swapping: number_1 = {number_1}, number_2 = {number_2}")
number_1, number_2 = number_2, number_1
print(f"After swapping: number_1 = {number_1}, number_2 = {number_2}")

print("\n")

"""
Exercise 5:
Temperature Conversion
Write a program to convert a temperature from Celsius to Fahrenheit. Use the formula:
F=(C×9/5)+32
Create a variable celsius to store the temperature in Celsius and print the result as:
"<celsius> degrees Celsius is equal to <fahrenheit> degrees Fahrenheit."
"""
temp_C = 25
temp_F = (temp_C*9/5) +32
print(f"{temp_C} degrees Celsius is equal to {temp_F} degrees Fahrenheit")

print("\n")

"""
Exercise 6:
Swapping Three Variables
Create three variables a, b, and c. Write a program to rotate their values such that:
a takes the value of b,
b takes the value of c,
c takes the value of a.
Print the values of a, b, and c before and after swapping.
"""
a = 2
b = 5
c = 0
print(f"Before swapping: a = {a}, b = {b}, c = {c}")
a, b, c = b, c, a
print(f"After swapping: a = {a}, b = {b}, c = {c}")

print("\n")

"""
Exercise 7:
Compound Interest Calculation
Write a program to calculate the amount of money after t years with compound interest. Use the formula:
A = P * ((1+ r/n))**(n*t)

Where:
- P is the principal amount.
- r is the annual interest rate (as a decimal, e.g., 5% = 0.05).
- n is the number of times interest is compounded per year.
- t is the time in years.
- A is the final amount.
Create variables P, r, n, and t, and calculate A. Print the result formatted as: "The amount after <t>
years is <A>."
"""
P = 142
r = 0.05
n = 12
t = 20
A = P * (1+ r/n)**(n*t)
print(f"The amount after {t} years is: {A}")

print("\n")

"""
Exercise 8:
Weighted Average
Create variables to store three grades: grade1, grade2, and grade3, and their respective weights: 
weight1, weight2, and weight3. Write a program to calculate the weighted average using the formula:
Weighted Average = ((grade_1*weight_1)+(grade_2*weight_2)+(grade_3*weight_3))/sum of weights
Print the result as: "The weighted average is <weighted_average>."
"""
grade_1 = 10
grade_2 = 5
grade_3 = 60
weight_1 = 3
weight_2 = 4
weight_3 = 1
sum_of_weights = weight_1 + weight_2 + weight_3

weighted_average = ((grade_1 * weight_1)+(grade_2 * weight_2)+(grade_3 * weight_3))/sum_of_weights
print(f"The weighted average is: {weighted_average}")

print("\n")

"""
Exercise 9:
Midpoint Between Two Points
Write a program to calculate the midpoint between two points (x1,y1) and (x2,y2). Use the formula:
midpoint = ((x1 +x2)/2, (y1 +y2)/2)
Create variables x1, y1, x2, and y2, and calculate the midpoint. Print the result as: "The midpoint 
between (<x1>, <y1>) and (<x2>, <y2>) is (<mid_x>, <mid_y>)."
"""
x1 = 1
x2 = 2
y1 = 11
y2 = 22
mid_x = (x1 +x2)/2
mid_y = (y1 +y2)/2
midpoint = (mid_x, mid_y)
print(f"The midpoint between ({x1}, {y1}) and ({x2}, {y2}) is ({mid_x}, {mid_y}).")

print("\n")

"""
Exercise 10:
Create three variables a, b, and c. Write a program to rotate their values such that:
- a takes the value of b;
- b takes the value of c;
- c takes the value of a.
Print the values of a, b, and c before and after swaping.
"""
a = 1
b = 2
c = 3
print(f"Variable values before swapping: a = {a}, b = {b}, c = {c}")
a, b, c = b, c, a
print(f"Variable values after swapping: a = {a}, b = {b}, c = {c}")

print("\n")

"""
Exercise 11:
Write a program to calculate the sum and product of the digits of a three-digit number.
For example:
1. Input: 123
2. Output:
      - sum of digits: 6
      - product of digits: 6 
"""
three_digit_number = 456
digit_1 = three_digit_number//100
digit_2 = (three_digit_number//10)%10
digit_3 = three_digit_number%10
sum_of_digits = digit_1 + digit_2 + digit_3
product_of_digits = digit_1 * digit_2 * digit_3
print(f"Sum of digits: {sum_of_digits}")
print(f"Product of digits: {product_of_digits}")

print("\n")

"""
Exercise 12:
Write a program that converts a temperature in Fahrenheit to both Celsius and Kelvin. Use the formulas:
C = (F-32)/1.8
K = C + 273.15
Create a variable fahrenheit and print the results as: 
"<fahrenheit>°F is equal to <celsius>°C and <kelvin>K
"""
temp_F = 56
temp_C = (temp_F - 32)/1.8
temp_K = temp_C + 273.15
print(f"{temp_F}°F is equal to {temp_C: .3f}°C and {temp_K: .2f}K")

print("\n")

"""
Exercise 13:
Write a program to calculate the hypotenuse of a right triangle given the lengths of the other two 
sides, a and b. Use the Pythagorean theorem:
c = sqrt(a**2 +b**2) 
"""
# Since there are different methods of import, for this exercise I decided to use two of them.
import math
from math import sqrt
a = 4
b = 80
# the calculation using the second import
c = sqrt(a**2 + b**2)
print(c)
# the calculation using the first import
d = math.sqrt((a**2 + b**2))
print(d)

print("\n")

"""
Exercise 14:
Write a program to calculate the sum of the first n terms of an arithmetic progression (AP). Use the 
formula: Sum = n/2 * (2a + (n-1)d)
Where:
- a is the first term of the AP
- d is the common difference
- n is the number of terms
Create variables a, d, and n, and calculate the sum. Print the result formatted as:
The sum of the first <n> terms of the AP is <sum>. 
"""
n = 9
a = 1
d = 2
Sum = n/2 * (2*a + (n-1)*d)
print(f"The sum of the first {n} terms of the AP is {Sum}")

print("\n")