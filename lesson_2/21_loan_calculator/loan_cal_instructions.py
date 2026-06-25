# Goal: determines the monthly payment
# Input: 
#       the loan amount (loan_amount; p)
#       the Annual Percentage Rate (APR) (apr) 
#               Should the user enter an interest rate of 5% as 5 or .05?
#       the loan duration (loan_duration_year)
# Operation:
#       monthly interest rate = APR / 12 (monthly_interest_rate; j) 
#       loan duration in months (loan_duration_months; n)
#       monthly payment (monthly_payment; m) = m = p * (j / (1 - (1 + j) ** (-n)))
# Output: 
#       monthly payment (monthly_payment; m)
#       print as a dollar and cents amount, e.g., $123.45 or $371.00.     
# Other: 
#       Run your code through Pylint and ask for code review if needed 
#       Edge cases: 
#               negative numbers 
#               no-interest loans: monthly_interest_rate = ''
#               loans that might be payable over a period of time that is not 
#               an integer number of years (e.g 2.5 years/30 months).
#               float(loan_duration_year) 
#       Use loan calculator to check your results 
#               https://www.calculator.net/loan-calculator.html     

##########################################################################
# Main structure: 
#       Outer loop: control the beg/end of the entire calculator 
#               Four nested loops: ask for and validate inputs
#                       Inputs: loan amount, apr, loan duration(yr), play again?
#               Operation: perform operation and display result  
#               break when answer == "n"
#       Four nested loops: ask for and validate inputs 
#               loan amount: invalid_number() function 
#               apr
#               loan duration(yr)
#               answer to another calculation: answer and answer[0] in ['y', 'n']
#               break when receiveing valid input 
#       Operation: 
#               monthly interest rate = APR / 12 (monthly_interest_rate; j) 
#               loan duration in months (loan_duration_months; n)
#               monthly payment (monthly_payment; m)
#               display result 

# Bonus features: 
#       Message: 
#               JSON
#               message() and prompt() function 
#       Allowing Floating-Point Numbers



 