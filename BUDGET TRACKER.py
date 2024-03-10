import os
import json
from datetime import datetime

# File path for storing transactions
TRANSACTIONS_FILE = "transactions.json"

# Function to load transactions from the file
def load_transactions():
    transactions = []
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "r") as file:
            transactions = json.load(file)
    return transactions

# Function to save transactions to the file
def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file)

# Function to record an income transaction
def add_income(transactions, amount, category):
    transaction = {
        "type": "income",
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print("Income recorded successfully!")

# Function to record an expense transaction
def add_expense(transactions, amount, category):
    transaction = {
        "type": "expense",
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print("Expense recorded successfully!")

# Function to calculate the remaining budget
def calculate_budget(transactions):
    income = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "income")
    expenses = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "expense")
    remaining_budget = income - expenses
    return remaining_budget

# Function to analyze expenses by category
def analyze_expenses(transactions):
    expense_categories = {}
    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            expense_categories[category] = expense_categories.get(category, 0) + transaction["amount"]

    if not expense_categories:
        print("No expenses recorded yet.")
    else:
        print("\nExpense Analysis:")
        for category, amount in expense_categories.items():
            print(f"{category}: ${amount}")

# Main function
def main():
    transactions = load_transactions()

    while True:
        print("\n=== BUDGET TRACKER ===")
        print("1. Record Income\n2. Record Expense\n3. Calculate Budget\n4. Analyze Expenses\n5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            add_income(transactions, amount, category)

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_expense(transactions, amount, category)

        elif choice == "3":
            remaining_budget = calculate_budget(transactions)
            print(f"\nRemaining Budget: ${remaining_budget}")

        elif choice == "4":
            analyze_expenses(transactions)

        elif choice == "5":
            print("Exiting Budget Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
