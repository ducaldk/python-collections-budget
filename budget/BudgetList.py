from . import Expense

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
    print(f"The count of all expenses: {len(myBudgetList)}")


# task 12
if __name__ == '__main__':
    main()

