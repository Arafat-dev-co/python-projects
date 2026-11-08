# Python Projects Portfolio

A collection of command-line applications built with pure Python, focusing on Object-Oriented Programming (OOP), file persistence (JSON), and clean architecture.

## Projects

### 1. Contact Manager (`contact.py`)
A CLI tool to manage contacts.
- **Features:** Add, view, search, update, and delete contacts.
- **Storage:** Saves data to `contacts.json`.
- **Validation:** Ensures names aren't empty, phone numbers are digits, and emails contain '@'.

### 2. Expense Tracker (`expense.py`)
A CLI tool to track daily spending.
- **Features:** Add expenses, view all, filter by category, and calculate total spending.
- **Storage:** Saves data to `expenses.json`.
- **Architecture:** Separates data (`Expense`) from logic (`ExpenseManager`).
