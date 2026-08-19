from datetime import datetime


class Expense:
    def __init__(self, amount, category, date):
        self.amount = float(amount)
        self.category = category.strip()
        self.date = date

    def __str__(self):
        return f"{self.amount:.2f} | {self.category} | {self.date}"

    def to_line(self):
        return f"{self.amount:.2f}|{self.category}|{self.date}"

    @classmethod
    def from_line(cls, line):
        parts = line.strip().split("|")

        if len(parts) != 3:
            raise ValueError("Invalid expense record.")

        amount = float(parts[0])
        category = parts[1].strip()
        date = parts[2].strip()

        datetime.strptime(date, "%Y-%m-%d")

        return cls(amount, category, date)
