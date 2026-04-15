import matplotlib.pyplot as plt

class Visualizer:
    def expense_pie_chart(self, categories, amounts):
        plt.figure(figsize=(6,6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title("Expenses by Category")
        plt.show()