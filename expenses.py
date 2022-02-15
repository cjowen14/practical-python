# expenses = [10.50, 8, 5, 15, 20, 5, 3]
# total = sum(expenses)

# for x in expenses:
#     sum+= x


expenses = []
num_expenses = int(input("Enter # of expenses: "))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("You spent $", total, " on lunch this week.", sep='')