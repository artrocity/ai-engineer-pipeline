# Exercise 2: Core Python Fundamentals (15-20 minutes)
# Today we're diving deeper into Python's core concepts!

# ===== LIST COMPREHENSIONS =====
# Think of list comprehensions like a recipe card - they're a compact way to create lists
# Format: [expression for item in iterable if condition]

# TODO: Create a list of squares for numbers 1-10 using list comprehension
squares = # Your code here

# TODO: Create a list of even numbers from 1-20 using list comprehension
evens = # Your code here

# TODO: Create a list of words that start with 'P' from the given list
words = ["Python", "Java", "Programming", "Code", "Pasta", "Pizza"]
p_words = # Your code here

print(f"Squares: {squares}")
print(f"Evens: {evens}")
print(f"P-words: {p_words}")

# ===== DICTIONARY COMPREHENSIONS =====
# Like list comprehensions, but for dictionaries!
# Format: {key_expr: value_expr for item in iterable}

# TODO: Create a dictionary where keys are numbers 1-5 and values are their cubes
cubes_dict = # Your code here

# TODO: Create a dictionary from two lists (keys and values)
keys = ["apple", "banana", "cherry"]
values = [5, 8, 3]
fruit_count = # Your code here

print(f"Cubes: {cubes_dict}")
print(f"Fruit count: {fruit_count}")

# ===== EXCEPTION HANDLING =====
# Think of try-except like wearing a helmet while biking - it protects you from crashes!

# TODO: Write a function that safely divides two numbers
# If division by zero occurs, return "Cannot divide by zero"
# If other errors occur, return "An error occurred"
def safe_divide(a, b):
    # Your code here with try-except
    pass

# TODO: Write a function that safely converts a string to an integer
# If conversion fails, return None
def safe_int_convert(string_num):
    # Your code here with try-except
    pass

# Test your exception handling
print(safe_divide(10, 2))    # Should print 5.0
print(safe_divide(10, 0))    # Should handle division by zero
print(safe_int_convert("123"))  # Should print 123
print(safe_int_convert("abc"))  # Should handle conversion error

# ===== FILE HANDLING =====
# Think of file handling like borrowing a library book - open it, read/write, then close it!

# TODO: Create a function that writes a list of favorite foods to a file
def write_foods_to_file(foods, filename):
    # Use 'with' statement to safely handle the file
    # Write each food on a new line
    pass

# TODO: Create a function that reads the foods back from the file
def read_foods_from_file(filename):
    # Use 'with' statement and handle potential file not found error
    # Return a list of foods (strip newline characters)
    pass

# Test your file handling
favorite_foods = ["Pizza", "Tacos", "Ice Cream", "Sushi"]
# TODO: Call your write function

# TODO: Call your read function and print the result


# ===== LAMBDA FUNCTIONS & MAP/FILTER =====
# Lambda functions are like quick sketches - small, anonymous functions for simple tasks

# TODO: Use map() with a lambda to convert a list of temperatures from Celsius to Fahrenheit
# Formula: F = C * 9/5 + 32
celsius_temps = [0, 20, 30, 40]
fahrenheit_temps = # Your code here using map and lambda

# TODO: Use filter() with a lambda to get only positive numbers
numbers = [-5, -2, 0, 3, 8, -1, 10]
positive_numbers = # Your code here using filter and lambda

print(f"Celsius: {celsius_temps}")
print(f"Fahrenheit: {list(fahrenheit_temps)}")
print(f"All numbers: {numbers}")
print(f"Positive only: {list(positive_numbers)}")

# ===== GENERATORS =====
# Generators are like a conveyor belt - they produce items one at a time, not all at once

# TODO: Create a generator function that yields even numbers up to a limit
def even_numbers_generator(limit):
    # Use yield instead of return
    # This should generate even numbers from 2 up to (but not including) limit
    pass

# TODO: Create a generator expression for squares of numbers 1-5
squares_gen = # Your code here (generator expression)

# Test your generators
print("Even numbers up to 10:")
for num in even_numbers_generator(10):
    print(num, end=" ")
print()

print("Squares generator:")
for square in squares_gen:
    print(square, end=" ")
print()

print("\n🎯 Core concepts practice complete!")