# Exercise 3: Advanced Applications (15-20 minutes)
# Time to combine concepts and tackle more challenging scenarios!

import json
from datetime import datetime
import time

# ===== ADVANCED CLASS DESIGN =====
# Let's create a more sophisticated class that uses multiple concepts

# TODO: Create a 'Library' class that manages books
class Library:
    def __init__(self):
        # TODO: Initialize an empty dictionary to store books
        # Key: book_id (string), Value: book info (dictionary)
        self.books = {}
    
    def list_books(self):
        # TODO: List all the books in the library
        # List all books in the library sorted
        for id, book in self.books.items():
            print(f'ID: {id} | Title: {book['title']},  Author: {book['author']},  Available {book['available']}')
        
    def add_book(self, book_id, title, author, year):
        # TODO: Add a book to the library
        # Create a dictionary with title, author, year, available (True by default)
        self.books[book_id] = {
            'title': title,
            'author': author,
            'year': year,
            'available': True
        }
    
    def remove_book(self, book_id):
        # TODO: Remove a book from the library
        try:
            del self.books[book_id]
        except KeyError as e:
            return 'Book for book id: {e} not found!'
        except Exception as e:
            return f'Error: {e}'
    
    def borrow_book(self, book_id):
        # TODO: Mark a book as not available (available = False)
        # Return success/failure message
        # Handle cases: book doesn't exist, book already borrowed
        
        # Get the book
        book = self.books.get(book_id)

        # Check if book isn't found
        if not book:
            return f'Error accessing book with an ID of {book_id}.'
        
        # Check if book is available
        if book['available'] == False:
            return f'Book: {book['title']} has already been checked out'
        
        # Check out the book
        book['available'] = False

        return f'Successfully checked out: {book['title']}'
    
    def return_book(self, book_id):
        # TODO: Mark a book as available (available = True)
        # Handle cases: book doesn't exist, book wasn't borrowed
        
        book = self.books.get(book_id)
        
        # Handle book doesn't exist
        if not book:
            return f'Book {book_id} does not exist!'
        
        # Handle book wasn't borrowed
        if book['available'] == True:
            return f'Book: {book['title']} was not checked out.'

        # Handle returning the book
        book['available'] = True
        
        return f'Successfully returned": {book['title']}'
    
    def search_books(self, search_term):
        # TODO: Return a list of book_ids where the search_term appears in title or author
        # Use list comprehension and make search case-insensitive

        matching_books = [
            key for key, value in self.books.items()
            if value['title'].lower() == search_term.lower() or 
            value['author'].lower() == search_term.lower()
            ]

        return matching_books
    
    def get_available_books(self):
        # TODO: Return a dictionary of only available books
        # Use dictionary comprehension
        
        available_books = {key: value for key, value in self.books.items() if value['available'] == True}

        return available_books
    
    def save_to_file(self, filename):
        # TODO: Save the library data to a JSON file
        # Use try-except for error handling
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.books, file)
            return f'Sucessfully wrote the list of books to file: {filename}'    
        except FileNotFoundError as f:
            return f'Unable to Save the file {f}'
        except Exception as e:
            return f'Error: {e}'
    
    def load_from_file(self, filename):
        # TODO: Load library data from a JSON file
        # Use try-except for error handling
        # Handle case where file doesn't exist
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.books = json.load(file)
            return f'Successfully loaded list of books from: {filename}'
        except FileNotFoundError:
            return f'Unable to locate file: {filename}'
        except Exception as e:
            return f'Error: {e}'

# ===== DATA PROCESSING CHALLENGE =====
# TODO: Create a function that processes student grades data

def analyze_student_grades(students_data):
    """
    Process student grades and return comprehensive statistics.
    
    Input format: 
    [
        {"name": "Alice", "grades": [85, 92, 78, 96]},
        {"name": "Bob", "grades": [76, 81, 88, 79]},
        ...
    ]
    
    Return a dictionary with:
    - student_averages: {name: average_grade}
    - class_average: overall average
    - top_student: name of student with highest average
    - grade_distribution: {"A": count, "B": count, ...} where A=90+, B=80-89, etc.
    """
    # TODO: Implement this function using multiple Python concepts:
    # - Dictionary/list comprehensions
    # - Lambda functions with map/filter
    # - Exception handling
    # - Built-in functions (max, min, etc.)

    
    result = {
        "student_averages": {},
        "class_average": 0,
        "top_student": "",
        "grade_distribution": {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    }
    
    # Student Averages
    result['student_averages'] = {
        student['name']: sum(student['grades']) / len(student['grades'])
        for student in students_data
    }

    # Class Average
    all_grades = [grade for student in students_data for grade in student['grades']]
    result['class_average'] = sum(all_grades) / len(all_grades)

    # Student with the highest average
    result['top_student'] = max(result['student_averages'], key=result['student_averages'].get())
    
    # Grade Distribution
    # Helper function to categorize a grade
    def get_letter_grade(grade):
        if grade >= 90: return "A"
        elif grade >= 80: return "B"
        elif grade >= 70: return "C"
        elif grade >= 60: return "D"
        else: return "F"

    # Count each letter grade
    for grade in all_grades: 
        letter = get_letter_grade(grade)
        result['grade_distribution'][letter] += 1
    return result

# ===== DECORATOR PRACTICE =====
# Decorators are like gift wrapping - they add functionality to existing functions

# TODO: Create a timing decorator that measures how long a function takes to execute
def timing_decorator(func):
    """A decorator that prints how long a function takes to execute."""
    
    def wrapper(*args, **kwargs):
        # TODO: Record start time, call function, record end time, print duration
        
        # Record start time
        start_time = time.time()

        # Call the original function and store it's results
        result = func(*args, **kwargs)

        # Record end time
        end_time = time.time()

        # Calculate duration
        duration = end_time - start_time

        # Output the time the functiont took
        print(f"Function '{func.__name__}' took {duration:.4f} seconds to execute")

        # Return the original function's results
        return result
    
    return wrapper

# TODO: Create a logging decorator that prints when a function is called
def logging_decorator(func):
    """A decorator that logs when a function is called."""
    def wrapper(*args, **kwargs):
        # TODO: Print function name and arguments, then call the function
        pass
    
    return wrapper

# TODO: Apply both decorators to this function
def slow_calculation(n):
    """A function that does some 'slow' calculation."""
    import time
    time.sleep(0.1)  # Simulate slow operation
    return sum(range(n))

# ===== CONTEXT MANAGER =====
# TODO: Create a simple context manager class for temporary file operations
class TempFileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        # TODO: Open the file and return the file object
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Close the file if it's open
        # Handle any cleanup needed
        pass

# ===== TESTING SECTION =====
if __name__ == "__main__":
    print("=== Testing Library Class ===")
    # TODO: Create a library instance and test all methods
    lib = Library()
    
    # Add some books
    lib.add_book(book_id=1 , title='Python for Dummies', author='Stef Maruch', year=2007)
    lib.add_book(book_id=2, title='Machine Learning for Dummies', author='Claude', year=2025)
    lib.add_book(book_id=3, title='Harry Potter 1', author='J. K. Rowling', year=1997)

    # Test Listing the books
    lib.list_books()

    # Test borrowing and returning
    print(lib.borrow_book(1))
    print(lib.return_book(1))

    # Test search functionality
    print(lib.search_books('PYTHON FOR DUMMIES'))
    print(lib.search_books('j. k. rowling'))

    # Test file operations
    print(lib.save_to_file('./fav_books.json'))
    print(lib.load_from_file('./fav_books.json'))

    
    print("\n=== Testing Grade Analysis ===")
    sample_students = [
        {"name": "Alice", "grades": [85, 92, 78, 96]},
        {"name": "Bob", "grades": [76, 81, 88, 79]},
        {"name": "Charlie", "grades": [95, 89, 93, 97]},
        {"name": "Diana", "grades": [67, 72, 70, 68]}
    ]
    
    # TODO: Call analyze_student_grades and print results
    
    print("\n=== Testing Decorators ===")
    # TODO: Call slow_calculation with decorators applied
    
    print("\n=== Testing Context Manager ===")
    # TODO: Use TempFileManager with 'with' statement
    
    print("\n🚀 Advanced applications complete!")