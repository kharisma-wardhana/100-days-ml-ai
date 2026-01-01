# Basic Python Variables and Functions
name = "John Doe"
age = 30
print(f"Name: {name}, Age: {age}")

def greet_user(name):
    return f"Hello, {name}!"

print(greet_user(name))

# Simple Arithmetic Operations
a = 10
b = 5
sum_result = a + b
product_result = a * b
print(f"Sum: {sum_result}, Product: {product_result}")

# List Manipulation
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print("Fruits List:", fruits)

# Looping through a list
for fruit in fruits:
    print(f"I like {fruit}")

# Basic Conditional Statements
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# Simple Function to Calculate Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(f"Factorial of 5: {factorial(5)}")

# Dictionary Usage
person = {
    "name": "Alice",
    "age": 28,
    "city": "New York"
}
print("Person Dictionary:", person)
print(f"{person['name']} lives in {person['city']}.")

# While Loop Example
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# Simple Class Definition
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())

# Importing and Using a Module
import math
print(f"Square root of 16 is: {math.sqrt(16)}")

# List Comprehension Example
squares = [x**2 for x in range(10)]
print("Squares from 0 to 9:", squares)

# Simple Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Lambda Function Example
add = lambda x, y: x + y
print(f"Sum using lambda: {add(3, 5)}")

# File Operations
with open("sample.txt", "w") as file:
    file.write("Hello, World!\nThis is a sample file.")

with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Simple List Sorting
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print("Sorted Numbers:", numbers)

# Using a Set to Remove Duplicates
duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(duplicates)
print("Unique Numbers:", unique_numbers)

# Basic String Manipulation
text = "Hello, Python!"
upper_text = text.upper()
print("Uppercase Text:", upper_text)
reversed_text = text[::-1]
print("Reversed Text:", reversed_text)

# Simple Date and Time Usage
import datetime
now = datetime.datetime.now()
print("Current Date and Time:", now)
print("Formatted Date:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Basic List Slicing
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = numbers_list[2:7]
print("Sliced List (2 to 6):", sliced_list)

# Simple Generator Function
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for number in countdown(5):
    print("Countdown:", number)

# Basic Tuple Usage
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)
x, y = coordinates
print(f"x: {x}, y: {y}")

# Simple Map Function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared Numbers using map:", squared_numbers)

# Basic Filter Function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers using filter:", even_numbers)

# Simple Reduce Function
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers using reduce:", product)

# Basic List Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined List:", combined_list)

# Simple Nested Function
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()
print("Nested Function Result:", outer_function("hello"))

# Basic Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)
print("Union of Sets:", union_set)
print("Intersection of Sets:", intersection_set)

# Simple List Reversal
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print("Reversed List:", reversed_list)

# Basic Zip Function
list_a = ['a', 'b', 'c']
list_b = [1, 2, 3]
zipped_list = list(zip(list_a, list_b))
print("Zipped List:", zipped_list)

# Simple Counter using Dictionary
def count_occurrences(items):
    counter = {}
    for item in items:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
occurrences = count_occurrences(items)
print("Item Occurrences:", occurrences)

# Basic List Insertion
my_list = [1, 2, 4, 5]
my_list.insert(2, 3)  # Insert 3 at index 2
print("List after Insertion:", my_list)

# Simple Palindrome Check
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print("Is 'A man a plan a canal Panama' a palindrome?", is_palindrome("A man a plan a canal Panama"))

# Basic Random Number Generation
import random
random_number = random.randint(1, 100)
print("Random Number between 1 and 100:", random_number)