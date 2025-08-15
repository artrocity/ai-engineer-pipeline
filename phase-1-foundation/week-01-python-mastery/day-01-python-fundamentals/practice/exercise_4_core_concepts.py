# Exercise 4: Core Python Fundamentals – Additional Practice (15-20 minutes)
# Build on your skills with these new challenges!

# ===== LIST COMPREHENSIONS =====
# TODO: Create a list of squares for even numbers 2-12 using list comprehension
square_list = [num ** 2 for num in range(2,13)]
print("=== SQUARE LIST TESTS ===")
print(square_list)

# TODO: Create a list of string lengths from the words below using list comprehension
word_collection = ["python", "programming", "list", "comprehension", "challenge", "data"]
string_length = [len(word) for word in word_collection]
print("=== STRING LENGTH TESTS ===")
print(string_length)

# TODO: Create a list of temperatures in Fahrenheit from Celsius values (F = C * 9/5 + 32)
celsius_temps = [0, 10, 20, 25, 30, 37, 100]
farenheit_temps = [(num * 1.8 + 32) for num in celsius_temps]
print("=== FARENHEIT CONVERSION TESTS ===")
print(farenheit_temps)

# ===== DICTIONARY COMPREHENSIONS =====
# TODO: Create a dictionary mapping each word to its vowel count
test_words = ["apple", "banana", "cherry", "date", "elderberry"]
vowels = ['a', 'e', 'i', 'o', 'u']

def count_vowels(word):
    return sum(1 for letter in word.lower() if letter in vowels)

vowel_dict = {word: count_vowels(word) for word in test_words}

print("=== VOWEL DICT TESTS ===")
print(vowel_dict)

# TODO: Create a dictionary from two lists: students and their grades
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
grades = [92, 87, 95, 78, 91]
student_grades = {student: grade for student, grade in zip(students, grades)}
print("=== STUDENT GRADES TESTS ===")
print(student_grades)


# ===== EXCEPTION HANDLING =====
# TODO: Write a function that calculates the average of a list, handling empty lists
def calculate_average(numbers):
    # Handle empty list
    if len(numbers) <= 0:
        return None
    
    # Calculate the average of the list
    return sum(numbers) / len(numbers)


print("=== AVERAGE CALCULATION TESTS ===")
print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([]))
print(calculate_average([10]))

# TODO: Write a function that safely accesses a dictionary key with a default value
def safe_dict_access(dictionary, key, default_value="Not found"):
    # Safel access dictionary, return Not Found if no key
    dict_key = dictionary.get(key, default_value)

    return dict_key


test_dict = {"name": "John", "age": 30, "city": "New York"}
print("\n=== DICTIONARY ACCESS TESTS ===")
print(safe_dict_access(test_dict, "name"))
print(safe_dict_access(test_dict, "country"))
print(safe_dict_access(test_dict, "salary", "Unknown"))

# ===== FILE HANDLING =====
# TODO: Write a function that creates a shopping list file from a list of items
shopping_items = ["milk", "bread", "eggs", "apples", "cheese", "yogurt"]

def create_shopping_list(items, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in items:
                file.write(f'{item}\n')
    except Exception as e:
        return 'Error: unable to create the file...'


print("\n=== SHOPPING LIST CREATION ===")
create_shopping_list(shopping_items, "shopping_list.txt")

# TODO: Write a function that reads a file and counts the number of lines
def count_file_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_count = 0
            for line in file.readlines():
                line_count += 1
            return line_count
    except FileNotFoundError:
        return 'Unable to locate requested file...'


print("\n=== LINE COUNTING TEST ===")
print(f"Lines in shopping list: {count_file_lines('shopping_list.txt')}")

# ===== LAMBDA FUNCTIONS & MAP/FILTER =====
# TODO: Use map() with a lambda to convert prices from dollars to euros (1 USD = 0.85 EUR)
usd_prices = [10.99, 25.50, 5.00, 100.00, 75.25]
euro_prices = list(map(lambda n: n * 0.85, usd_prices))


print("\n=== CURRENCY CONVERSION ===")
print("USD prices:", usd_prices)
print("EUR prices:", euro_prices) 

# TODO: Use filter() with a lambda to get products that cost more than $20
products = [
    {"name": "Book", "price": 15.99},
    {"name": "Headphones", "price": 89.99},
    {"name": "Notebook", "price": 5.99},
    {"name": "Keyboard", "price": 45.00},
    {"name": "Mouse", "price": 12.50}
]

expensive_products = list(filter(lambda i: i['price'] > 20, products))
print("\n=== EXPENSIVE PRODUCTS ===")
print(expensive_products)

# ===== GENERATORS =====
# TODO: Create a generator function that yields even numbers up to a given limit
def even_generator(limit):
    return (num for num in range(1, limit) if num % 2 == 0)
even_nums = even_generator(20)

print("\n=== EVEN NUMBERS UP TO 20 ===")
for num in even_nums:
    print(num)

# TODO: Create a generator expression that yields the first letter of each name
names_list = ["Alexander", "Beatrice", "Christopher", "Delilah", "Emmanuel", "Francesca"]
name_expression = (letter[0] for letter in names_list)

print("\n=== FIRST LETTERS ===")
for i in name_expression:
    print(i)

# TODO: Combine multiple concepts - create a function that:
# 1. Takes a list of sentences
# 2. Returns a dictionary where keys are sentence lengths and values the sentences
# 3. Use exception handling for edge cases
sentences = [
    "Python is awesome.",
    "I love coding.",
    "List comprehensions are powerful.",
    "Generators save memory.",
    "Exception handling prevents crashes.",
    "Functions make code reusable."
]

def group_sentences_by_length(sentence_list):
    try:
        sentence_dict = {len(sentence): sentence for sentence in sentence_list}
        return sentence_dict
    except ValueError:
        return 'Error...'
    except Exception as e:
        return f'Error: {e}'


print("\n=== SENTENCES GROUPED BY LENGTH ===")
print(group_sentences_by_length(sentences))