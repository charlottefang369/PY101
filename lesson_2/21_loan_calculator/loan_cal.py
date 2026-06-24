
# Helper functions: 


import json

with open('loan_calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[message]

def prompt(message):
    print(f'==>{message}')

def invalid_number(number_str):
    try: 
        float(number_str)
    except ValueError:
        return True 
    return False 

while True: 
    prompt(messages("welcome"))

    # Loop1: loan amount
    while True: 
        prompt(messages("loan_amount"))
        loan_amount = input()

        if not invalid_number(loan_amount):
            break 

        prompt(messages("invalid_number"))

    loan_amount = float(loan_amount)

    # Loop2: APR
    while True: 
        prompt(messages("apr"))
        apr = input()

        if not invalid_number(apr):
            break 

        prompt(messages("invalid_number"))
        
    monthly_interest_rate = float(apr) / 12

    # Loop3: loan duration in years
    while True: 
        prompt(messages("duration_in_years"))
        loan_duration_year = input()
        
        if not invalid_number(loan_duration_year):
            break 

        prompt(messages("invalid_number"))

    loan_duration_months = float(loan_duration_year) * 12


    # Operation
    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate)) ** (-1 * loan_duration_months))
    output = round(monthly_payment, 2)

    prompt(messages('result').format(output=output))


    # Loop4: Play again? 
    while True:
        prompt(messages("another_calculation"))
        answer = input().lower()

        if answer and answer[0] in ['y', 'n']:
            break

        prompt(messages("invalid_number"))
    
    if answer == 'n':
        break 
