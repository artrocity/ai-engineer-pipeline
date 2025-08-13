# Exercise 1: Prior Knowledge Review (10-15 minutes)
# Let's warm up by reviewing what you already know!

# ===== DATA TYPES REVIEW =====
# TODO: Create variables of each basic data type and print their types
# Hint: Use type() function to check data types

# Create a string variable
string_var = 'This is a string'
print(f'Variable: {string_var} is of type: {type(string_var)}')

# Create an integer variable
int_var = 87
print(f'Variable: {int_var} is of type: {type(int_var)}')

# Create a float variable
float_var = 76.9
print(f'Variable: {float_var} is of type: {type(float_var)}')


# Create a boolean variable
bool_var = True
print(f'Variable: {bool_var} is of type: {type(bool_var)}')

# Create a list with mixed data types
mixed_list = [3, 'abc', True, 76.3]
print(f'Variable: {mixed_list} is of type: {type(mixed_list)}')


# Create a dictionary with at least 3 key-value pairs
rand_dict = {
    'key1': 'Value',
    'key2': True,
    'key3': 76
}
print(f'Variable: {rand_dict} is of type: {type(rand_dict)}')


# ===== BASIC FUNCTIONS REVIEW =====
# TODO: Write a function that takes two numbers and returns their sum
def add_numbers(num1:int, num2:int) -> int:
    sum = num1 + num2
    return print(f'The sum of {num1} + {num2} is: {sum}')


# TODO: Write a function that takes a name and returns a greeting
# Example: greet("Alice") should return "Hello, Alice!"
def greet(name:str) -> str:
    return print(f'Hello, {name}!')


# TODO: Write a function that takes a list of numbers and returns the largest one
# Don't use the built-in max() function - write your own logic!
def find_maximum(num_list:list) -> int:
    max_num = 0

    for num in num_list:
        if num > max_num:
            max_num = num
    
    return print(f'The maximum number in the list is: {max_num}')


# ===== BASIC OOP REVIEW =====
# TODO: Create a simple class called 'Student' with the following:
# - Attributes: name, age, grade
# - Method: introduce() that prints "Hi, I'm [name], I'm [age] years old and I'm in grade [grade]"

class Student:
    # TODO: Write the __init__ method
    def __init__(self, name:str, age:int, grade:int):
        self.name = name
        self.age = age
        self.grade = grade
    
    # TODO: Write the introduce method
    def introduce(self) -> str:
        return print(f"Hi, I'm {self.name}, I'm {self.age} years old, and I'm in grade {self.grade}")


# TODO: Create an instance of Student and call the introduce method
new_student = Student(name='Jane', age=18, grade=12)

# ===== TEST YOUR WORK =====
if __name__ == "__main__":
    # TODO: Test all your functions and classes here
    # Call add_numbers with two numbers
    add_numbers(4,7)
    # Call greet with your name
    greet('Ryan')
    # Call find_maximum with a list of numbers
    list_of_numbers = [1, 3, 122, 39, 48, 298]
    find_maximum(list_of_numbers)
    # Create a student and have them introduce themselves
    new_student.introduce()
    print("Great job reviewing the basics! 🎉")