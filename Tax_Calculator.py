def get_bracket(monthly_pay):
    bracket = 0
    if monthly_pay <= 20833:  
        bracket = 1
    elif monthly_pay <= 33333: 
        bracket = 2
    elif monthly_pay <= 66666:
        bracket = 3
    elif monthly_pay <= 166666:
        bracket = 4
    elif monthly_pay <= 666666:
        bracket = 5
    elif monthly_pay > 666666:
        bracket = 6
    else:
        print('Invalid Monthly Pay!')

    return bracket

def get_annual_tax(annual_pay):
    tax = 0
    if annual_pay <= 250000:  
        tax = 0
    elif annual_pay <= 400000: 
        tax = 0.15 * annual_pay
    elif annual_pay <= 800000:
        tax = 22500 + (0.2 * annual_pay)
    elif annual_pay <= 2000000:
        tax = 102500 + (0.25 * annual_pay)
    elif annual_pay <= 8000000:
        tax = 402500 + (0.3 * annual_pay)
    elif annual_pay > 8000000:
        tax = 2202500 + (0.35 *annual_pay)
    else:
        print('Invalid Annual Pay!')

    return tax

def get_monthly_tax(monthly_pay):
    tax = 0
    if monthly_pay <= 20833:  
        tax = 0
    elif monthly_pay <= 33333: 
        tax = 0.15 * monthly_pay
    elif monthly_pay <= 66666:
        tax = 1875 + (0.2 * monthly_pay)
    elif monthly_pay <= 166666:
        tax = 8541.8 + (0.25 * monthly_pay)
    elif monthly_pay <= 666666:
        tax = 33541.8 + (0.3 * monthly_pay)
    elif monthly_pay > 666666:
        tax = 183541.8 + (0.35 *monthly_pay)
    else:
        print('Invalid Monthly Pay!')

    return tax

monthly_income = float(input("Input your monthly income: "))
tax_bracket = get_bracket(monthly_income)
monthly_tax = get_monthly_tax(monthly_income)
annual_income = monthly_income * 12.0
annual_tax = get_annual_tax(annual_income)


net_monthly = monthly_income - monthly_tax
net_annually = annual_income - annual_tax

print("With your %.2f monthly income\nYou have an annual income of %.2f\n" % (monthly_income, annual_income))
print("Your tax bracket is %d\nYour monthly income tax is %.2f\nYour annual income tax is %.2f\n" % (tax_bracket, monthly_tax, annual_tax))
print("Your monthly net pay is %.2f\nYour annual net pay is %.2f\n" % (net_monthly, net_annually))
