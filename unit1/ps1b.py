balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_cc_interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

min_monthly_payment = 0
remaining_balance = 0
monthly_interest = annual_cc_interest / 12.0
month = 1
while(remaining_balance >= 0):
    min_monthly_payment = min_monthly_payment + 10
    remaining_balance = balance
    for i in range(1, 13):
        remaining_balance = round(remaining_balance * (1 + monthly_interest) - min_monthly_payment, 2)
        if(remaining_balance <= 0):
            month = i
            break

print("RESULT")
print("Monthly payment to pay off debt in 1 year: " + str(min_monthly_payment))
print("Number of months needed: " + str(month))
print("Balance: " + str(remaining_balance))
