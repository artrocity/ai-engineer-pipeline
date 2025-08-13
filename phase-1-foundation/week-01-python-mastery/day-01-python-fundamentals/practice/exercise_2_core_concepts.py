# Exercise 2: Core Python Fundamentals (15-20 minutes)
# Today we're diving deeper into Python's core concepts!

# ===== LIST COMPREHENSIONS =====
# Think of list comprehensions like a recipe card - they're a compact way to create lists
# Format: [expression for item in iterable if condition]

# TODO: Create a list of squares for numbers 1-10 using list comprehension
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [num * num for num in num_list]

# TODO: Create a list of even numbers from 1-20 using list comprehension
num_list_to_20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
evens = [num for num in num_list_to_20 if num % 2 == 0] 

# TODO: Create a list of words that start with 'P' from the given list
words = ["Python", "Java", "Programming", "Code", "Pasta", "Pizza"]
p_words = [word for word in words if word[0] == 'P']

print(f"Squares: {squares}")
print(f"Evens: {evens}")
print(f"P-words: {p_words}")

# ===== DICTIONARY COMPREHENSIONS =====
# Like list comprehensions, but for dictionaries!
# Format: {key_expr: value_expr for item in iterable}

# TODO: Create a dictionary where keys are numbers 1-5 and values are their cubes
cubes_dict = {num: num * num * num for num in range(1,6)}

# TODO: Create a dictionary from two lists (keys and values)
keys = ["apple", "banana", "cherry"]
values = [5, 8, 3]
fruit_count = {key: value for key, value in zip(keys, values)}

print(f"Cubes: {cubes_dict}")
print(f"Fruit count: {fruit_count}")


# ===== EXCEPTION HANDLING =====
# Think of try-except like wearing a helmet while biking - it protects you from crashes!

# TODO: Write a function that safely divides two numbers
# If division by zero occurs, return "Cannot divide by zero"
# If other errors occur, return "An error occurred"
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return 'Cannot Divide by Zero'
    except Exception as e:
        return f'An error occured: {e}'

# TODO: Write a function that safely converts a string to an integer
# If conversion fails, return None
def safe_int_convert(string_num):
    try:
        number = int(string_num)
        return number
    except ValueError:
        return None
    except Exception as e:
        return f'An error occured: {e}'

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
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for food in foods:
                file.write(f'{food}\n')
    except FileNotFoundError:
        return f'File: {filename} not found!'

# TODO: Create a function that reads the foods back from the file
def read_foods_from_file(filename):
    # Use 'with' statement and handle potential file not found error
    # Return a list of foods (strip newline characters)
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return f'File: {filename} not found!'

# Test your file handling
favorite_foods = ["Pizza", "Tacos", "Ice Cream", "Sushi"]
# TODO: Call your write function
# write_foods_to_file(foods=favorite_foods, filename='./fav_foods.txt')
# TODO: Call your read function and print the result
read_foods_from_file('./fav_foods.txt')

# ===== LAMBDA FUNCTIONS & MAP/FILTER =====
# Lambda functions are like quick sketches - small, anonymous functions for simple tasks
# Template lambda arguments: expression

# TODO: Use map() with a lambda to convert a list of temperatures from Celsius to Fahrenheit
# Formula: F = C * 9/5 + 32
celsius_temps = [0, 20, 30, 40]
fahrenheit_temps = map(lambda c: c * 9/5 + 32, celsius_temps)

# TODO: Use filter() with a lambda to get only positive numbers
numbers = [-5, -2, 0, 3, 8, -1, 10]
positive_numbers = filter(lambda n: n > 0, numbers)

print(f"Celsius: {celsius_temps}")
print(f"Fahrenheit: {list(fahrenheit_temps)}")
print(f"All numbers: {numbers}")
print(f"Positive only: {list(positive_numbers)}")

# ===== GENERATORS =====
# Generators are like a conveyor belt - they produce items one at a time, not all at once

# TODO: Create a generator function that yields even numbers up to a limit
def even_numbers_generator(limit):
    for num in range(2, limit, 2):
        yield num

# TODO: Create a generator expression for squares of numbers 1-5
squares_gen = (num*num for num in range(1,6))

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
