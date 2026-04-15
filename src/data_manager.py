import csv
import os

class DataManager:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['day', 'month', 'year', 'income', 'expense', 'category'])
                writer.writeheader()

    def get_expenses_by_category(self):
        expenses = {}
        try:
            with open(self.csv_path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    category = row.get('category', 'Other')
                    expense_str = row.get('expense', '0')
                    expense = float(expense_str) if expense_str else 0
                    expenses[category] = expenses.get(category, 0) + expense
        except:
            pass
        return expenses

    def add_transaction(self, type_, amount):
        from datetime import datetime
        now = datetime.now()
        data = {
            'day': str(now.day),
            'month': str(now.month),
            'year': str(now.year),
            'income': '',
            'expense': '',
            'category': 'General'
        }
        if type_ == 'Income':
            data['income'] = str(amount)
        elif type_ == 'Expense':
            data['expense'] = str(amount)
        try:
            with open(self.csv_path, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['day', 'month', 'year', 'income', 'expense', 'category'])
                if os.path.getsize(self.csv_path) == 0:
                    writer.writeheader()
                writer.writerow(data)
        except:
            pass