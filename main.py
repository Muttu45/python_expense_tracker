import re
from datetime import datetime

from modules.expense import Expense
from modules.file_operations import load_expenses, save_expense
from modules.category_summarizer import summarize_by_category


DATE_PATTERN = r"^\d{4}-\d{2}-\d{2}$"


def display_menu():
    print("\n" + "=" * 35)
    print("       EXPENSE TRACKER")
    print("=" * 35)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summarize by Category")
    print("4. Exit")
    print("=" * 35)


def get_amount():
    while True:
        value = input("Enter amount: ").strip()

        try:
            amount = float(value)

            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Please enter a numeric value.")


def get_category():
    while True:
        category = input("Enter category: ").strip()

        if category:
            return category

        print("Category cannot be empty. Please try again.")


def get_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            if not re.fullmatch(DATE_PATTERN, date):
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Invalid date. Please enter a valid date.")


def add_expense(expenses):
    print("\n--- Add Expense ---")

    amount = get_amount()
    category = get_category()
    date = get_date()

    expense = Expense(amount, category, date)

    if save_expense(expense):
        expenses.append(expense)
        print("Expense added successfully!")
    else:
        print("Unable to save expense.")


def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'Amount':<12}{'Category':<20}{'Date'}")
    print("-" * 45)

    for expense in expenses:
        print(
            f"{expense.amount:<12.2f}"
            f"{expense.category:<20}"
            f"{expense.date}"
        )


def show_summary(expenses):
    print("\n--- Expense Summary by Category ---")

    if not expenses:
        print("No expenses to summarize.")
        return

    summary = summarize_by_category(expenses)

    print(f"{'Category':<20}{'Total Amount'}")
    print("-" * 35)

    for category, total in summary.items():
        print(f"{category:<20}{total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_summary(expenses)

        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
