import math


# Step 1:Multiply the net balance shown on the statement by the number of days in
# the billing cycle.
# Step 2:Multiply the net payment received by the number of days the payment was
# received before the end of the billing cycle. (days before end cycle = days
#                                                                        in billing cycle – day of payment)
# Step 3:Subtract the result of the calculation in step 2 from the result of the
# calculation in step 1.
# Step 4:Divide the result of step 3 by the number of days in the billing cycle, the


def interest():
    air = float(input("What is your annual interest rate? "))
    billingDays = int(input("What is the number of days in your billing cycle? "))
    previousNetBalance = float(input("What is your previous net balance? "))
    paymentAmount = float(input("What is your payment amount? "))
    dayPaymentMade = int(input("What is the day in which your payment will be made? "))
    multiAmount = previousNetBalance * billingDays
    daysEndCycle = billingDays - dayPaymentMade
    multiNetPay = paymentAmount * daysEndCycle
    product3 = multiAmount - multiNetPay
    divProd = product3 / billingDays
    monthlyRate = air/12
    interestCharge = divProd * (monthlyRate/100)

    print("Your monthly interest charge is $",math.floor(interestCharge*100)/100)
interest()