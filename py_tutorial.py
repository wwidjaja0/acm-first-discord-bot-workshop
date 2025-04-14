# Python Tutorial: Data Types, Variables, Functions, and Modules

# -------------------------------
# 1. Data Types
# -------------------------------

# Integer: Whole numbers
import math as m
from math import pow
import math
age = 25
print("Integer:", age)

# Float: Decimal numbers
pi = 3.14
print("Float:", pi)

# Boolean: True or False values
is_student = True
print("Boolean:", is_student)

# String: Sequence of characters
greeting = "Hello, World!"
print("String:", greeting)

# List: Ordered, mutable collection
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# NoneType: Represents the absence of a value
nothing = None
print("NoneType:", nothing)

# -------------------------------
# 2. Variables
# -------------------------------

# Variables are created when you assign a value to them
x = 10
print("Initial value of x:", x)

# Variables can change type after assignment
x = "Now I'm a string"
print("Changed value of x:", x)

# Variable names are case-sensitive
name = "Alice"
Name = "Bob"
print("name:", name)
print("Name:", Name)

# -------------------------------
# 3. Functions
# -------------------------------

# Defining a function using the 'def' keyword


def greet():
    print("Hello from the greet function!")


# Calling the function
greet()

# Function with parameters (arguments)


def greet_person(name):
    print("Hello, " + name + "!")


greet_person("Charlie")

# Function with multiple parameters


def add_numbers(a, b):
    result = a + b
    print("Sum:", result)


add_numbers(5, 3)

# Function with keyword arguments


def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type + " named " + pet_name + ".")


describe_pet(animal_type="hamster", pet_name="Harry")

# Function with a return value


def multiply(x, y):
    return x * y


product = multiply(4, 5)
print("Product:", product)

# -------------------------------
# 4. Modules
# -------------------------------

# Modules are files containing Python code (functions, variables, etc.)
# To use a module, you import it

# Importing the entire module
print("Square root of 16:", math.sqrt(16))

# Importing a specific function from a module
print("2 raised to the power 3:", pow(2, 3))

# Importing a module with an alias
print("Cosine of 0:", m.cos(0))

# Creating and using a custom module:
# Suppose you have a file named 'my_module.py' with the following content:
# def say_hello():
#     print("Hello from my_module!")

# You can import and use it as follows:
# import my_module
# my_module.say_hello()

# Note: Ensure 'my_module.py' is in the same directory as this script.

# -------------------------------
# End of Tutorial
# -------------------------------

input("\n\nPress Enter to proceed to your bot...")
