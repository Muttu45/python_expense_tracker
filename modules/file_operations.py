from pathlib import Path

from .expense import Expense


DATA_FILE = Path("data/expenses.txt")


def load_expenses():
    expenses = []

    try:
        if not DATA_FILE.exists():
            return expenses

        with DATA_FILE.open("r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                try:
                    expense = Expense.from_line(line)
                    expenses.append(expense)

                except (ValueError, IndexError):
                    continue

    except FileNotFoundError:
        return []

    except PermissionError:
        return []

    except OSError:
        return []

    return expenses


def save_expense(expense):
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with DATA_FILE.open("a", encoding="utf-8") as file:
            file.write(expense.to_line() + "\n")

        return True

    except (PermissionError, OSError):
        return False
