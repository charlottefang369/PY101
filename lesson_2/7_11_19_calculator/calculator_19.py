
# Program Requirements
#       Input: 
#               Ask the user for two numbers:
#                       number1 and number2
#                       Allowing Floating-Point Numbers.
#               Ask the user for the type of operation to perform: 
#                       1) add, 2) subtract, 3)multiply 4)divide
#               Ask the user if want another calculation after disaplying the result:
#                       y or n 
#               Create functions and loops to validate inputs:
#                       number1, number2, operation type, answer to if want another calculation
#       Operation: Perform the calculation and display the result
#       Message: 
#               Prefix each message with a ==> marker 
#               Extracting messages in the program to a configuration file.
#               Internationalization: allow message to be displayed in multiple language 
##########################################################################
# Main structure: 
#       Outer loop: control the beg/end of the entire calculator 
#               Four nested loops: ask for and validate inputs
#                       Inputs: number1, number2, operation and answer to another calculation
#               Operation: perform operation and display result  
#               break when answer == "n"
#       Four nested loops: ask for and validate inputs 
#               number1 & number2: invalid_number() function 
#               operation: operation in ["1", "2", "3", "4"]
#               answer to another calculation: answer and answer[0] in ['y', 'n']
#               break when receiveing valid input 
#       Operation: 
#               match case statement 
#               display result 

# Bonus features: 
#       Message: 
#               JSON
#               message() and prompt() function 
#               Multilingual options 
#       Allowing Floating-Point Numbers
##########################################################################


# Helper functions: 
import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang='en'):
    return MESSAGES[lang][message]

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False


# Main Structure 
prompt(messages('welcome'))

# Outer loop 
while True:
   
    # Loop 1 (numer1)
    while True:
        prompt(messages('number_prompt_1'))
        number1 = input()

        if not invalid_number(number1):     # We want the this loop to end asa we get a valid number
            break                           # For an valid number, the function invalid_number(number1) returns False
        prompt(messages('invalid_number'))  # That's why we negate it here with not invalid_number(number1) to represent a valid number
    
    # Loop 2 (number2)
    while True:
        prompt(messages('number_prompt_2'))
        number2 = input()

        if not invalid_number(number2):
            break

        prompt(messages('invalid_number'))
    
    # Loop 3 (operation)
    while True:
        prompt(messages('operation_prompt'))
        operation = input()

        if operation in ["1", "2", "3", "4"]:
            break

        prompt(messages('invalid_operation'))
    
    # Operation 
    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    output = round(output, 2)  # Round the result to two decimals

    prompt(messages('result').format(output=output))
    
    #Loop 4 (another operation)
    while True:
        prompt(messages('another_operation'))
        answer = input().lower()

        if answer and answer[0] in ['y', 'n']:
            break

        prompt(messages('invalid_answer'))
    
    if answer == 'n':
        break 