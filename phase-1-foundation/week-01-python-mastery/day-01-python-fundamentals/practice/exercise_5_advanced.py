import json
from typing import List, Dict
import datetime

# ===== LIST COMPREHENSIONS =====
# TODO: Create a list of book titles with more than 10 characters
book_titles = ["Python 101", "Data Science Handbook", "AI Basics", "Deep Learning Guide", "Clean Code"]
# TODO: Your list comprehension here
large_titles = [title for title in book_titles if len(title) > 10]
print('===== LIST COMPREHENSION =====')
print(large_titles)

# TODO: Create a list of book years that are even numbers
book_years = [1999, 2001, 2010, 2015, 2022]
# TODO: Your list comprehension here
even_years = [year for year in book_years if year % 2 == 0]


# ===== DICTIONARY COMPREHENSIONS =====
# TODO: Create a dictionary using the two lists below
authors = ["Alice", "Bob", "Charlie", "David", "Eva"]
titles = ['Alice in Wonderland', 'Bob the Builder', 'Charlies Angels', 'David & Goliath', 'Eva in Wonderland']
# TODO: Your dictionary comprehension here
books = {author: title for author, title in zip(authors, titles)}
print('===== DICT COMPREHENSION =====')
print(books)

# TODO: Create a dictionary associating the number of books published in that year
year = [1900, 2021, 2022, 2023]
books_published = [1234, 5432, 3333, 1357]
# TODO: Your dictionary comprehension here
book_years_dict = {year: books for year, books in zip(year, books_published)}
print(book_years_dict)

# ===== EXCEPTION HANDLING =====
# TODO: Write a function that converts a string input to a floating-point rating
def safe_float_convert(input_str):
    try:
        return float(input_str)
    except TypeError as e:
        return f'Error: {e}'
    except Exception as e:
        return f'Error: {e}'
    
print('===== EXCEPTIONS =====')
print(safe_float_convert('7'))
print(safe_float_convert('abc'))

# ===== FILE HANDLING =====
import json

# TODO: Write a function that opens a file containing book info and returns the content
def read_books_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as fe:
        return 'Unable to open file...'

# TODO: Write a function that writes a list of favorite books to a file
def write_books_to_file(books, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(books, file)
    except Exception as e:
        return f'Error: {e}'

print('===== FILE HANDLING =====')
print(read_books_file('fav_books.json'))
write_books_to_file('fav_books.json', book_years_dict)

# ===== LAMBDA FUNCTIONS & MAP/FILTER =====
page_counts = [120, 250, 360, 410]
# TODO: Use map() with a lambda to double the page counts
double_pages = map(lambda n: n * 2, page_counts)

# TODO: Use filter() with a lambda to get books published after the year 2000
def read_book_filter(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        books_list = list(data.values())
        new_books = filter(lambda book: book['year'] > 2000, books_list)
        return list(new_books)
    except Exception as e:
        return f'Error: {e}'

print('===== LAMBDAS / FILTER =====')
print(list(double_pages))
print(read_book_filter('fav_books.json'))

# ===== GENERATORS =====
# TODO: Create a generator function that yields book titles starting with a vowel
def vowel_books_generator(titles: List[str]):
    pass  # Your implementation here

# TODO: Create a generator expression for lengths of each book title
# TODO: Your generator expression here

# ===== CLASS & METHODS =====
class BookManager:
    def __init__(self):
        self.books = []  # list of book dictionaries

    # TODO: Add a book with title, author, year, pages
    def add_book(self, title: str, author: str, year: int, pages: int):
        pass

    # TODO: Remove a book by title
    def remove_book(self, title: str) -> bool:
        pass

    # TODO: Search books by author (case-insensitive)
    def search_by_author(self, author: str) -> List[Dict]:
        pass

    # TODO: Calculate average number of pages
    def average_pages(self) -> float:
        pass

    # TODO: Get oldest book(s) in collection
    def oldest_books(self) -> List[Dict]:
        pass

    # TODO: Save the book collection to a JSON file
    def save_data(self, filename: str):
        pass

    # TODO: Load the book collection from a JSON file
    def load_data(self, filename: str):
        pass
