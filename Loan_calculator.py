Loan_amount = float(input("What is the loan amount"))
Intrest_rate = float(input("Intrest Rate"))
Payment = float(input("Monthly payment"))
months= int(input("How many months you want to see result for"))

monthly_rate = Intrest_rate/100/12 

for i in range(months):
    interest_paid = Loan_amount * monthly_rate
    Loan_amount =  Loan_amount + interest_paid 

    if (Loan_amount - Payment < 0 ):
        print("the last payment is", Loan_amount)
        print("you paid of", i+1, "month")
        break
    Loan_amount = Loan_amount - Payment


    print("paid", Payment, "of which" , interest_paid, "was intrest") 
    print(" Now I owe", Loan_amount)