expenses = []
n = int(input("How many expenses?"))
for i in range(n):
    amount = float(input("Enter expense:"))
    expenses.append(amount)
total = 0
for i in expenses:
    total = total + i
highest = expenses[0]
lowest = expenses[0]
for i in expenses:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
average = total / len(expenses)
print("Total Expense:", total)
print("Highest EXpense:", highest)
print("Lowest Expense:", lowest)
print("Average Expense:", average)


        

