def summarize_by_category(expenses):
    summary = {}

    for expense in expenses:
        category = expense.category

        if category not in summary:
            summary[category] = 0.0

        summary[category] += expense.amount

    return summary
