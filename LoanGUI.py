import tkinter as tk
def calculate_loan():
    interestRate = float(interestRateEntry.get()) / 100
    numYears = int(numYearEntry.get())
    loanAmount = float(loan_amount_entry.get())
    numPayements = numYears * 12
    monthlyInterestRate = interestRate / 12
    monthlyPayments = (monthlyInterestRate * loanAmount) / (1 - (1 + monthlyInterestRate) ** -numPayements)
    totalPayments = monthlyPayments * numPayements 
    monthlyPaymentLables.config(text = f'Monthly payment: ${monthlyPayments:.2f}')
    total_payment_label.config(text = f'Total payment: ${totalPayments:.2f}')

window = tk.Tk()
window.title('Loan Payment Calculator')
interest_rate_label = tk.Label(window, text = 'Annual Interest Rate (%):')
num_years_label = tk.Label(window, text = 'Number of Years:')
loanAmountLables = tk.Label(window, text = 'Loan Amount ($):')
monthlyPaymentLables = tk.Label(window, text = '')
total_payment_label = tk.Label(window, text = '')
interestRateEntry = tk.Entry(window)
numYearEntry = tk.Entry(window)
loan_amount_entry = tk.Entry(window)
calculateButton = tk.Button(window, text = 'Calculate', command = calculate_loan)
interest_rate_label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
num_years_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
loanAmountLables.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
interestRateEntry.grid(row = 0, column = 1, padx = 5, pady = 5)
numYearEntry.grid(row = 1, column = 1, padx = 5, pady = 5)
loan_amount_entry.grid(row = 2, column = 1, padx = 5, pady = 5)
calculateButton.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
monthlyPaymentLables.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)
total_payment_label.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
window.mainloop()


