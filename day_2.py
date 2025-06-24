"""
Exercise 1:
Read a string of characters from the user and:
- display the string length
- display how many empty spaces are in the string
- change the first half of the string into capital letters and the second half in lowercase letters
"""
print("Exercise 1: ")

user_string = input("Type a sentence: ")    # string from the user
print(f"The string length is: {len(user_string)} characters")   # displayed string length
print(f"In the string are {user_string.count(" ")} empty spaces")  # displayed empty spaces in the string

# half of string written with capital letters and half with lowercase letters
print(user_string[:len(user_string)//2].upper() + user_string[len(user_string)//2:].lower())

print("\n")

"""
Exercise 2:
Write a Python program to:
- create a tuple containing the names of five cities.
- convert the tuple into a list.
- add a new city to the list.
- replace the second city in the list with another city of your choice.
- convert the list back into a tuple and print the final tuple.
"""
print("Exercise 2: ")

cities = ("Paris", "Dubai", "Tokyo", "Rome", "Barcelona") # tuple containing the names of 5 cities
list_cities = list(cities)    # the tuple 'cities' converted into a list
print(type(list_cities))
# option 1 to add a new city to a list:
list_cities.append("Singapore")
# option 2 to add a new city to a list:
list_cities.extend(["Los Angeles"])
print(list_cities)

list_cities[1] = "Bali"  # the second city 'Dubai' was replaced by 'Bali'
print(list_cities)
convert_list_cities_to_tuple = tuple(list_cities) # the list was converted back into a tuple
print(type(convert_list_cities_to_tuple))

print("\n")

"""
Exercise 3:
Write a Python program to: 
- create a dictionary with the names of three people as keys and their ages as values.
- access the age of a specific person by their name (key).
- add a new person with their age to the dictionary.
- replace the age of one of the existing people.
- remove a specific person from the dictionary.
- print the updated dictionary.
"""
print("Exercise 3: ")

# dictionary with 3 key-value (name-age) pairs:
a_dictionary = {
    "Zeus": 50,
    "Persephone": 20,
    "Hades": 30
}

# option 1 to access the age of a specific person
print(f"The age of Zeus is: {a_dictionary["Zeus"]}")

# option 2 to access the age of a specific person
print(f"The age of Zeus is: {a_dictionary.get("Zeus")}")

a_dictionary["Aphrodite"] = 25      # a new person was added to the dictionary
print(a_dictionary)

a_dictionary["Hades"] = 35     # the age of an existing person was changed
print(a_dictionary)

# option 1 to remove a specific person from the dictionary
a_dictionary.pop("Persephone")
print(f"This is the updated dictionary: {a_dictionary}")   # updated dictionary after the first remove

# option 2 to remove a specific person from the dictionary
del a_dictionary["Hades"]
print(f"This is the updated dictionary: {a_dictionary}")   # updated dictionary after the first remove

print("\n")

"""
Exercise 4:
Given the following dictionary:
my_students = {
    'John': {
        'grades': [['Math', [10]], ['Romanian', [5, 7]], ['History', [10, 8]]],
        'school': "Nr 1",
        'parents': ('Laurentiu', 'Ana'),
        'olympic': True
    },
    'Alice': {
        'grades': [['Math', [10, 7]],
                   ['Romanian', [5, 7]],
                   ['History', [10, 8]]],
        'school': 'Nr 2',
        'parents': ('Ion', 'Ana'),
        'olympic': False
    }
}

1. Access and print the names of John's parents.
2. Add a new grade (9) for the subject 'Romanian' in Alice's record.
3. Update John's school name to "Nr 3".
"""
print("Exercise 4: ")

my_students = {
    'John': {
        'grades': [['Math', [10]], ['Romanian', [5, 7]], ['History', [10, 8]]],
        'school': "Nr 1",
        'parents': ('Laurentiu', 'Ana'),
        'olympic': True
    },
    'Alice': {
        'grades': [['Math', [10, 7]],
                   ['Romanian', [5, 7]],
                   ['History', [10, 8]]],
        'school': 'Nr 2',
        'parents': ('Ion', 'Ana'),
        'olympic': False
    }
}

print(f"The names of John parents: {my_students['John']['parents']}")  # Access and print the names of John's parents
my_students['Alice']['grades'][1][1].append(9)  # grade 9 was added in the subject 'Romanian' for Alice
print(my_students['Alice'])
my_students['John']['school'] = 'Nr 3'  # John's school was change from Nr 1 to Nr 3
print(my_students['John'])

print("\n")

"""
Exercise 5:
Given the following list:
my_animals = ['dog', 'cat', 'elephant_1', 'mouse', 'elephant_2', 'zebra', 'racoon', 'tiger', 'cow', 'sheep']

1. Print all animals from my_animals list
2. Ignore printing the "elephants" and if you get the "tiger" abort mission
"""
print("Exercise 5: ")

my_animals = ['dog', 'cat', 'elephant_1', 'mouse', 'elephant_2', 'zebra', 'racoon', 'tiger',
              'cow', 'sheep']

print(my_animals)   # print all animals from my_animal list

# display's all animals except 'elephant' and when it reaches to 'tiger' it breaks the loop:
for animal in my_animals:
    if 'elephant' in animal:
        continue
    elif 'tiger' in animal:
        break
    print(animal)
