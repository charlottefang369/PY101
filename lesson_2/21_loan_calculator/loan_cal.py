
# Helper functions:

import json

with open('loan_cal_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[message]

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f'Value must be > 0: {number_str}') #The f string part is here to help programmer to debug not to show the user 
    except ValueError:
        return True
    
    return False

def invalid_number_rate(number_str):
    try:
        number = float(number_str)
        if number < 0:
            raise ValueError(f'Value must be >= 0: {number_str}') #The f string part is here to help programmer to debug not to show the user 
    except ValueError:
        return True
    
    return False

prompt(messages("welcome"))

while True:
    prompt("---------------------------------")

    # Loop1: loan amount
    while True:
        prompt(messages("loan_amount"))
        amount = input()

        if not invalid_number(amount):
            break

        prompt(messages("invalid_number"))

    
    # Loop2: APR
    while True:
        prompt(messages("apr"))
        prompt(messages('apr_example'))
        interest_rate = input() 

        if not invalid_number_rate(interest_rate):
            break

        prompt(messages("invalid_number"))


    # Loop3: loan duration in years
    while True:
        prompt(messages("duration_in_years"))
        prompt(messages("duration_in_years_example"))
        years = input()

        if not invalid_number(years):
            break

        prompt(messages("invalid_number"))

    
    # Operation
    loan_amount = float(amount)
    annual_interest_rate = float(interest_rate) / 100
    monthly_interest_rate = annual_interest_rate / 12
    months = float(years) * 12

    if monthly_interest_rate == 0: 
        monthly_payment = loan_amount / months
    else:
        monthly_payment = loan_amount * (
            monthly_interest_rate / 
            (1 - (1 + monthly_interest_rate)**(-months))
            )
    
    prompt(messages('result').format(monthly_payment=monthly_payment)) #the 2f portion in message replaced the original code: output = round(output, 2) 


    # Loop4: Play again?
    while True:
        prompt(messages("another_calculation"))
        answer = input().lower()

        if answer and answer[0] in ['y', 'n']:
            break

        prompt(messages("invalid_number"))

    if answer[0] == 'n':
        break
