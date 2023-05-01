from . import Expense
import matplotlib.pyplot as plt
import timeit

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()
    if not divided_for_loop == divided_set_comp:
        print("Sets are NOT equal by == test")

    for a,b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print("Sets are NOT equal by subset test")

    # Note annoying embedded indent problem at first...
    print(timeit.timeit(stmt="expenses.categorize_for_loop()", setup='''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
''', number=100000, globals=globals()))

    print(timeit.timeit(stmt="expenses.categorize_set_comprehension()", setup='''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
''', number=100000, globals=globals()))





if __name__ == "__main__":
    main()