# Exercise 3: Advanced Applications (15-20 minutes)
# Time to combine concepts and tackle more challenging scenarios!

import json
from datetime import datetime

# ===== ADVANCED CLASS DESIGN =====
# Let's create a more sophisticated class that uses multiple concepts

# TODO: Create a 'Library' class that manages books
class Library:
    def __init__(self):
        # TODO: Initialize an empty dictionary to store books
        # Key: book_id (string), Value: book info (dictionary)
        pass
    
    def add_book(self, book_id, title, author, year):
        # TODO: Add a book to the library
        # Create a dictionary with title, author, year, available (True by default)
        pass
    
    def remove_book(self, book_id):
        # TODO: Remove a book from the library
        # Handle case where book doesn't exist (use try-except or if-else)
        pass
    
    def borrow_book(self, book_id):
        # TODO: Mark a book as not available (available = False)
        # Return success/failure message
        # Handle cases: book doesn't exist, book already borrowed
        pass
    
    def return_book(self, book_id):
        # TODO: Mark a book as available (available = True)
        # Handle cases: book doesn't exist, book wasn't borrowed
        pass
    
    def search_books(self, search_term):
        # TODO: Return a list of book_ids where the search_term appears in title or author
        # Use list comprehension and make search case-insensitive
        pass
    
    def get_available_books(self):
        # TODO: Return a dictionary of only available books
        # Use dictionary comprehension
        pass
    
    def save_to_file(self, filename):
        # TODO: Save the library data to a JSON file
        # Use try-except for error handling
        pass
    
    def load_from_file(self, filename):
        # TODO: Load library data from a JSON file
        # Use try-except for error handling
        # Handle case where file doesn't exist
        pass

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
    
    # Your implementation here
    
    return result

# ===== DECORATOR PRACTICE =====
# Decorators are like gift wrapping - they add functionality to existing functions

# TODO: Create a timing decorator that measures how long a function takes to execute
def timing_decorator(func):
    """A decorator that prints how long a function takes to execute."""
    # Import time module at the top if needed
    import time
    
    def wrapper(*args, **kwargs):
        # TODO: Record start time, call function, record end time, print duration
        pass
    
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
    # Test borrowing and returning
    # Test search functionality
    # Test file operations
    
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