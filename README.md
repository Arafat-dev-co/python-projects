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

### 3. To-Do List (`task.py`)
A CLI tool to manage daily tasks.
- **Features:** Add tasks, view tasks with status indicators (`[X]` or `[ ]`), and mark tasks as completed.
- **Storage:** Saves data to `tasks.json`.
- **Architecture:** Uses boolean flags to track task states across sessions.

### 4. Student Gradebook (`student.py`)
A CLI tool to manage student grades.
- **Features:** Add students with 3 grades, view all students with their averages, and calculate the overall class average.
- **Storage:** Saves data to `grades.csv`.
- **Architecture:** Uses the `csv` module with `DictReader` and `DictWriter` to handle CSV files safely. Includes custom string-to-list and list-to-string parsing.

### 5. File Organizer (`file.py`)
An automation script that cleans up messy folders.
- **Features:** Scans a directory and automatically moves files into categorized subfolders (Images, Documents, Videos, Audio, Misc).
- **Architecture:** Uses `os` and `shutil` modules to interact with the operating system, create directories dynamically, and move files safely.

### 6. Web Scraper (`scraper.py`)
An automation script that extracts data from the internet.
- **Features:** Scrapes quotes and authors from `quotes.toscrape.com` and saves them to a CSV file.
- **Libraries:** Uses `requests` to download the HTML and `BeautifulSoup` to parse and extract specific elements.


