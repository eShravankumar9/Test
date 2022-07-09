#total = 0
#expenses = []
#for i in range(7):
#    expenses.append(float(input("Enter your Expense")))
    
#total = sum(expenses)

#print ("your toatl Expense:"+ str(total))

total = 0
expenses = []
num_expenses = int(input("Enter number of Expences"))
for i in range(num_expenses):
    expenses.append(float(input("Enter your Expense")))
    
total = sum(expenses)

print ("your toatl Expense:"+ str(total))