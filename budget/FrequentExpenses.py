from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()

expenses.read_expenses('data/spending_data.csv')

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

print("Task 6")
spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)
categories, count = zip(*top5)

print("Task 7")
# fig is the 'top level container' for the plots
fig, ax = plt.subplots()

print("Task 8")
ax.bar(categories, count)
ax.set_title(r'# of Purchases by Category')

print("Task 9")
plt.show()

