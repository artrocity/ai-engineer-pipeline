# Exercise 3: Core Python Fundamentals – Reinforcement Practice (15-20 minutes)
# Time to strengthen your skills with fresh challenges!

# ===== LIST COMPREHENSIONS =====
# TODO: Create a list of cubes for numbers 1–7 using list comprehension
cubed_list = [num**3 for num in range(1,8)]
print(f'=====CUBED LIST=====')
print(cubed_list)

# TODO: Create a list of odd numbers from 1–15 using list comprehension
odd_list = [num for num in range(1,16) if num % 2 !=0]
print(f'=====ODD LIST=====')
print(odd_list)

# TODO: Create a list of names that end with the letter 'a'
names = ["Olivia", "Noah", "Mia", "Liam", "Sophia", "Ethan", "MARIANNA"]
a_names = [name for name in names if name.endswith('a')]
print(f'=====NAMES LIST=====')
print(a_names)

# ===== DICTIONARY COMPREHENSIONS =====
# TODO: Create a dictionary mapping numbers 1–5 to their factorials
import math
fact_dict = {item: math.factorial(item) for item in range(1,6)}
print(f'=====FACTORIAL DICT=====')
print(fact_dict)

# TODO: Combine two lists into a dictionary of country: capital
countries = ["Japan", "France", "Brazil"]
capitals = ["Tokyo", "Paris", "Brasília"]

capitals_dict = dict(zip(countries, capitals))
print(f'=====CAPITAL LIST=====')
print(capitals_dict)

# ===== EXCEPTION HANDLING =====
# TODO: Write a function that reads an integer from a string and returns double the value
def double_number_from_string(input_str):
    try:
        return int(input_str) * 2
    except ValueError as v:
        return 'Error: input must be convertible to a number / int'
        
    
print(f'=====CONVERT INT TO STRING=====')
print(double_number_from_string("12"))
print(double_number_from_string("abc"))

# TODO: Write a function that opens a file and returns the first line
def read_first_line_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readline()
    except FileNotFoundError:
        return 'Unable to locate file...'

print(f'=====FIRST LINE OF A FILE=====')
print(read_first_line_from_file('./fav_foods.txt'))

# ===== FILE HANDLING =====
# TODO: Write a function that appends a list of tasks to a file, one task per line
tasks_list = ['write book', 'workout', 'study python']

def append_tasks_to_file(tasks, filename):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            for task in tasks:
                file.write(f'{task}\n')
        return 'Success! Check the file log!'
    except FileNotFoundError:
        return 'unable to locate and write to file...'

print(f'=====WRITE TO A FILE=====')
append_tasks_to_file(tasks=tasks_list, filename='./to_do_list.txt')

# TODO: Write a function that reads tasks from a file into a list
def read_tasks_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError as f_error:
        return f'Unable to locate file...{f_error}'

print(f'=====READ TASKS FROM A FILE=====')
print(read_tasks_from_file(filename='./to_do_list.txt'))

# ===== LAMBDA FUNCTIONS & MAP/FILTER =====
# TODO: Use map() with a lambda to convert a list of kilometers to miles (1 km = 0.621371 miles)
km_list = [10, 40, 50, 80]
km_to_miles = map(lambda n: n * 0.621371, km_list)

print(f'=====Kilometers=====')
print(km_list)
print(f'=====Miles=====')
print(list(km_to_miles))

# TODO: Use filter() with a lambda to get words longer than 5 letters from a list
words_list = ["cat", "elephant", "dog", "butterfly", "ant", "rhinoceros", "bee", "penguin"]
longer_than_5 = filter(lambda w: len(w) > 5, words_list)
print(f'=====Words longer than 5 letters=====')
print(list(longer_than_5))

# ===== GENERATORS =====
# TODO: Create a generator function that yields multiples of 3 up to a given limit
def multiples_of_three_generator(limit):
    for n in range(1, limit):
        if n % 3 == 0:
            yield n

print(f'=====GENERATOR FUNCTION=====')
for num in multiples_of_three_generator(21):
    print(num)

# TODO: Create a generator expression that yields the reverse of each string in a list
reverse_words = (''.join(reversed(word)) for word in words_list)

print(f'=====GENERATOR EXPRESSION=====')
for word in reverse_words:
    print(word)

