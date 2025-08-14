# Mini Project: Personal Expense Tracker (30-45 minutes)
# Build a command-line expense tracking application that demonstrates all core Python concepts!

import json
import datetime
from typing import List, Dict, Optional

class ExpenseTracker:
    """
    A personal expense tracker that manages financial transactions.
    Think of this like a digital wallet that remembers every purchase!
    """
    
    def __init__(self, data_file: str = "expenses.json"):
        self.data_file = data_file
        self.expenses = []  # List of expense dictionaries
        self.categories = set()  # Set of unique categories
        self.load_data()
    
    def add_expense(self, amount: float, category: str, description: str, date: str = None):
        """
        Add a new expense to the tracker.
        
        TODO: Implement this method to:
        1. Create an expense dictionary with: id, amount, category, description, date
        2. Add the category to self.categories set
        3. Append the expense to self.expenses list
        4. Auto-generate an ID (use len(self.expenses) + 1)
        5. Use today's date if no date provided (use datetime.date.today().isoformat())
        """
        # Your implementation here
        pass
    
    def remove_expense(self, expense_id: int):
        """
        Remove an expense by ID.
        
        TODO: Implement this method to:
        1. Find and remove the expense with matching ID
        2. Return True if successful, False if expense not found
        3. Use list comprehension to filter out the expense
        """
        # Your implementation here
        pass
    
    def get_expenses_by_category(self, category: str) -> List[Dict]:
        """
        Get all expenses for a specific category.
        
        TODO: Use list comprehension to return expenses matching the category
        Make the search case-insensitive
        """
        # Your implementation here
        pass
    
    def get_expenses_by_date_range(self, start_date: str, end_date: str) -> List[Dict]:
        """
        Get expenses within a date range (inclusive).
        
        TODO: Use list comprehension to filter expenses by date
        Dates are in 'YYYY-MM-DD' format, so string comparison works!
        """
        # Your implementation here
        pass
    
    def calculate_total_by_category(self) -> Dict[str, float]:
        """
        Calculate total spending per category.
        
        TODO: Use dictionary comprehension to create category totals
        Hint: For each category, sum all expenses in that category
        """
        # Your implementation here
        pass
    
    def calculate_monthly_totals(self) -> Dict[str, float]:
        """
        Calculate total spending per month.
        
        TODO: Group expenses by year-month (e.g., '2024-03') and sum amounts
        Use dictionary comprehension and date string slicing
        """
        # Your implementation here
        pass
    
    def get_top_expenses(self, n: int = 5) -> List[Dict]:
        """
        Get the top N highest expenses.
        
        TODO: Sort expenses by amount (descending) and return top N
        Use sorted() with lambda function
        """
        # Your implementation here
        pass
    
    def search_expenses(self, search_term: str) -> List[Dict]:
        """
        Search expenses by description (case-insensitive).
        
        TODO: Use list comprehension with case-insensitive search
        """
        # Your implementation here
        pass
    
    def generate_summary_report(self) -> str:
        """
        Generate a comprehensive summary report.
        
        TODO: Create a formatted string report including:
        1. Total number of expenses
        2. Total amount spent
        3. Average expense amount
        4. Top spending category
        5. Most expensive single purchase
        6. Date range of expenses
        
        Use f-strings for formatting and the methods you've already created!
        """
        # Your implementation here
        pass
    
    def save_data(self):
        """
        Save expenses to JSON file.
        
        TODO: Use json.dump() with proper exception handling
        Convert set to list for JSON serialization (categories)
        """
        try:
            # Your implementation here
            pass
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def load_data(self):
        """
        Load expenses from JSON file.
        
        TODO: Use json.load() with exception handling
        Handle case where file doesn't exist
        Convert categories list back to set if loading
        """
        try:
            # Your implementation here
            pass
        except FileNotFoundError:
            # Initialize with empty data if file doesn't exist
            print(f"No existing data file found. Starting fresh!")
            self.expenses = []
            self.categories = set()
        except Exception as e:
            print(f"Error loading data: {e}")
            self.expenses = []
            self.categories = set()

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("       💰 PERSONAL EXPENSE TRACKER 💰")
    print("="*50)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expenses by Category")
    print("4. View Expenses by Date Range")
    print("5. Search Expenses")
    print("6. Generate Summary Report")
    print("7. View Top Expenses")
    print("8. Remove Expense")
    print("9. Save & Exit")
    print("-"*50)

def get_user_input(prompt: str, input_type: type = str):
    """
    Get user input with type validation and exception handling.
    
    TODO: Implement input validation:
    1. Keep asking for input until valid
    2. Handle ValueError for type conversion
    3. Return the converted value
    """
    while True:
        try:
            # Your implementation here
            pass
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None

def main():
    """
    Main application loop.
    
    TODO: Implement the command-line interface:
    1. Create ExpenseTracker instance
    2. Display menu in a loop
    3. Handle user choices
    4. Call appropriate methods based on user selection
    5. Handle all menu options with proper input validation
    """
    
    # Create the expense tracker
    tracker = ExpenseTracker()
    
    print("Welcome to your Personal Expense Tracker!")
    
    while True:
        display_menu()
        choice = get_user_input("Enter your choice (1-9): ", int)
        
        if choice is None:  # User cancelled
            continue
            
        # TODO: Implement all menu options
        if choice == 1:
            # Add expense
            pass
            
        elif choice == 2:
            # View all expenses
            pass
            
        elif choice == 3:
            # View expenses by category
            pass
            
        elif choice == 4:
            # View expenses by date range
            pass
            
        elif choice == 5:
            # Search expenses
            pass
            
        elif choice == 6:
            # Generate summary report
            pass
            
        elif choice == 7:
            # View top expenses
            pass
            
        elif choice == 8:
            # Remove expense
            pass
            
        elif choice == 9:
            # Save and exit
            tracker.save_data()
            print("Data saved! Thanks for using Expense Tracker! 🎉")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

# ===== HELPER FUNCTIONS =====
# TODO: Create these utility functions to make your code cleaner

def format_expense(expense: Dict) -> str:
    """Format an expense dictionary for display."""
    # Return a nicely formatted string representation of an expense
    pass

def format_currency(amount: float) -> str:
    """Format a number as currency."""
    # Return amount formatted as currency (e.g., "$123.45")
    pass

def validate_date(date_string: str) -> bool:
    """Validate if a string is a valid date in YYYY-MM-DD format."""
    # Use try-except with datetime.datetime.strptime()
    pass

# ===== BONUS CHALLENGES =====
# If you finish early, try implementing these additional features:

def export_to_csv(tracker: ExpenseTracker, filename: str):
    """Export expenses to CSV file."""
    # TODO: Use csv module to write expenses to a CSV file
    pass

def import_from_csv(tracker: ExpenseTracker, filename: str):
    """Import expenses from CSV file."""
    # TODO: Use csv module to read expenses from a CSV file
    pass

def plot_expenses_by_category(tracker: ExpenseTracker):
    """Create a simple bar chart of expenses by category using matplotlib."""
    # TODO: Create a visual representation using matplotlib
    pass

# ===== RUN THE APPLICATION =====
if __name__ == "__main__":
    main()

# ===== SUCCESS CRITERIA =====
"""
🎯 This mini-project should demonstrate:

✅ Classes and methods
✅ List and dictionary comprehensions  
✅ Exception handling (try-except)
✅ File I/O operations
✅ JSON serialization
✅ Lambda functions and sorting
✅ String formatting (f-strings)
✅ Type hints
✅ User input validation
✅ Data filtering and searching
✅ Mathematical operations and statistics

🌟 Bonus points for:
- Clean, readable code with good variable names
- Helpful user interface with clear prompts
- Robust error handling
- Additional creative features

"""