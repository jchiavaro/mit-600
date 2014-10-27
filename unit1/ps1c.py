balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_cc_interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

low = balance / 12
high =  (balance * (1 + (annual_cc_interest / 12)) ** 12) / 12
min_monthly_payment = 0
while(True):
    remaining_balance = balance
    min_monthly_payment = (low + high)/2.0
    for i in range(1, 13):
        interest = round(balance * annual_cc_interest / 12, 2)
        remaining_balance +=  interest - min_monthly_payment
        if(remaining_balance <= 0):
            break

    if(high-low < 0.005 ):
        print "RESULT"
        min_monthly_payment = round(min_monthly_payment + 0.004999, 2)
        print "Monthly payment to pay off debt in 1 year:", round(min_monthly_payment, 2)

        remaining_balance = balance

        for month in range(1,13):
            interest = round(balance * annual_cc_interest / 12, 2)
            remaining_balance += interest - min_monthly_payment
            if balance <= 0:
                break
        print "Number of months needed:", month
        print "Balance:", round(remaining_balance, 2)
        break
    elif remaining_balance < 0:
        high = min_monthly_payment
    else:
        low = min_monthly_payment
