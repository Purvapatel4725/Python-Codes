Intrest_rate = float(input("interest rate: ")) 
no_years = float(input("number of years: "))
loan_amt = float(input("loan amount: "))
numerator = loan_amt * Intrest_rate
months = no_years*12
addition = 1 + Intrest_rate
raise_to = addition ** months
divide_by_one = 1 / raise_to
sub_by_one = 1 - divide_by_one
simplified = numerator / sub_by_one
answer = simplified * no_years * 12
print("Monthly Payment of the loan will be:",simplified)
print("The total paymennt of the loan will be:",answer)

