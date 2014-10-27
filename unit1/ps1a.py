# Problem Set 1 
# Name: Jorge Chiavaro 
# Collaborators: 
# Time Spent: 0:45

balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_cc_interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
minimum_monthly_interest = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
remaining_balance = balance
interest_paid = 0
principal_paid = 0
total_paid = 0
for i in range(1, 13):
    minimum_monthly_payment = round(minimum_monthly_interest * remaining_balance, 2)
    interest_paid = round((annual_cc_interest / 12.0) * remaining_balance, 2)
    principal_paid = minimum_monthly_payment - interest_paid
    remaining_balance = remaining_balance - principal_paid
    total_paid = total_paid + principal_paid + interest_paid
    print("Month: " + str(i))
    print("Minimum monthly payment: $" + str(minimum_monthly_payment))
    print("Principle paid: $" + str(principal_paid))
    print("Remaining balance: $" + str(remaining_balance))

print("RESULT")
print("Total amount paid: $" + str(total_paid));
print("Remaining balance: $" + str(remaining_balance));
