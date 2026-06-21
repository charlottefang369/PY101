#1 Prefix each message with a => marker
#2 Replace if/else statement with match case statement.
#3 Create a function to validate that the input is valid, and use that function
# to create the looping mechanism for validating numbers and operations.



def prompt(message):              #1: Add helper function
    print(f"==> {message}")

def invalid_number(number_str):   #3: Add helper function
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):            #3 Add loop to validate number input 
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):            #3 Add loop to validate number input 
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt("What operation would you like to perform?\n1) Add 2) Subtract " \
"3) Multiply 4) Divide")
operation = input()

while operation not in ["1", "2", "3", "4"]:  #3 Add loop to validate operation input 
    prompt("You must choose 1, 2, 3, or 4")
    operation = input()

match operation:           #2:Replace if statement with match case statement
        output = int(number1) + int(number2)
    case "2":
        output = int(number1) - int(number2)
    case "3":
        output = int(number1) * int(number2)
    case "4":
        output = int(number1) / int(number2)

prompt(f"The result is {output}")