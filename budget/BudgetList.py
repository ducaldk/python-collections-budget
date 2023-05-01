from . import Expense
import matplotlib.pyplot as plt

class BudgetList:
    
    # task 1, 2
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.sum_overages = 0
        self.overages = []
        self.expenses = []

    # task 3,4,5
    def append(self, item):
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item

    # task 6
    def __len__(self):
        return len(self.expenses)+len(self.overages)
    
    # module 3 tasks 1,2
    def __iter__(self):
        # not explained in the instructions but figure-outable?
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self
    
    # module 3 tasks 4,5
    def __next__(self):
        try:
            # this was not acceptable to the test but passed the boundary conditions
            # return next(self.iter_e)
            return self.iter_e.__next__()
        except StopIteration as stop:
            # this was not acceptable to the test but passed the boundary conditions
            # return next(self.iter_o)
            return self.iter_o.__next__()

    

# task 7
def main():
    myBudgetList = BudgetList(1200)
    # task 8,9 
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')

    # task 10
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    # task 11
    print( "The count of all expenses: " + str(len(myBudgetList)))
    # print(f"The count of all expenses: {len(myBudgetList)}")

    # module 3, task 5
    for entry in myBudgetList:
        print(entry)

    # module 3, task 7
    fig, ax = plt.subplots()

    # module 3, task 8
    labels = [ 'Expenses', 'Overages', 'Budget']
    # module 3, task 9
    values = [ myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]
    # module 3, task 10
    ax.bar(labels, values, color=['green','red','blue'])
    # module 3, task 11
    ax.set_title('Your total expenses vs. total budget')
    # module 3, task 12
    plt.show()


# task 12
if __name__ == '__main__':
    main()

