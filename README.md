# Manager

# Project Overview and Structure
This project provides a simple command-line system for individuals to manage daily financial entries without complex database configurations.
Folder Structure:
expense_tracker/
data/expenses.txt
src/init.py
src/file_handler.py
src/validator.py
src/tracker.py
src/analytics.py
tests/test_tracker.py
main.py
statement.md
README.md
# Key Features
Dual Transaction Tracking: Log both Income and Expense transactions with automated timestamps and custom categories.
Flat File Persistence: Saves and retrieves records from a local text file at data/expenses.txt.
Financial Analytics: Displays total income, total expenditure, net available balance, and highlights the highest spending category.
Robust Error Handling: Prevents application crashes by validating numeric inputs and menu options.
Automated Testing: Integrated unit testing for core validation logic.
How to Run the Application
# Prerequisites:
Python 3.x installed on your system.
Execution Commands:
Clone the Repository:
git clone your-repository-url
cd expense_tracker
Run the App:
python main.py
Run Unit Tests:
python -m unittest tests/test_tracker.py
# Testing Approach
Unit tests are implemented using Python native unittest module in tests/test_tracker.py:
Validates positive transaction amounts.
Catches invalid string inputs and negative numbers.
Verifies boundary selections for CLI navigation.
License
Created for academic evaluation and open-source learning.
