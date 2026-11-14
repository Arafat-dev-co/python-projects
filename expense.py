import json 

class Expense:
    def __init__(self, item_name, amount, category, date):
        self.item_name = item_name
        self.amount = amount
        self.category = category
        self.date = date

 
    def to_dict(self):
        return {
            "item_name": self.item_name,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    def __str__(self):
        return f"Date: {self.date} | Item: {self.item_name} | Category: {self.category} | Amount: {self.amount:.2f}"


class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.filename = "expenses.json"

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as f:
                contents = json.load(f)

            for item in contents:
                user = Expense(item["item_name"], item["amount"], item["category"], item["date"])
                self.expenses.append(user)

        except FileNotFoundError:
            pass


    def save_expenses(self):
        data_to_save = []

        for spend in self.expenses:
            data_to_save.append(spend.to_dict())

        with open(self.filename, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    def add_expense(self, expense):
        self.expenses.append(expense)
            
    def get_all_expenses(self):
        return self.expenses

    def calculate_total(self):
        total = 0

        for spend in self.expenses:
            total += spend.amount
        return total

def main():
    manager = ExpenseManager()
    manager.load_expenses()

    while True:
        print("---EXPENSE TRACKER---")
        print("1. Add Expense")
        print("2. View all Expenses")
        print("3. View by category")
        print("4. Show Total Spending")
        print("5. Exit")

        option = int(input("Choose: "))

        if option == 1:
            item_name = input("Enter item name: ")

            amount = float(input("Enter the amount: "))

            category = input("Enter the category: ")

            date = input("Enter the date: ")

            user = Expense(item_name, amount, category, date)
            manager.add_expense(user)
            manager.save_expenses()
            print("Expense added!")

        elif option == 2:
            spend = manager.get_all_expenses()
            if len(spend) == 0:
                print("No expenses recorded")
            else:
                for exp in spend:
                    print(exp)
        
        elif option == 3:
            search_cat = input("Enter category to search: ")
            expenses = manager.get_all_expenses()
            found = False
            for exp in expenses:
                if exp.category.lower() == search_cat.lower():
                    print(exp)
                    found = True
            if not found:
                print("No expenses found in this categoey")


        elif option == 4:
            user = manager.calculate_total()
            print(f"Total Spending: ${user:.2f}")

        elif option == 5:
            print("Thanks for using ExpenseTracfor ker\n")
            break

        else:
            print("Invalid choice. Please enter 1 - 5")                        

if __name__ == "__main__":
    main()