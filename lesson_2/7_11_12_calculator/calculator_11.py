#1 Prefix each message with a ==> marker.
#2 Replace if/else statement with match case statement.
#3 Create a function to validate if the input is valid. 
#4 Use that function to create the looping mechanism for numbers and operations.



def prompt(message):              #1: Add helper function
    print(f"==> {message}")

def invalid_number(number_str):   #3: Add helper function
    try:
        int(number_str)
    except ValueError:            # What kind of input will raise an error for int()? And what kind of error?
        return True               # Empty string, non-numeric string, float-looking string
    return False                  # These all raise ValueError, so ValueError is the error we want to catch.

prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):            #4 Add loop to validate number1 input 
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):            #3 Add loop to validate number2 input 
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt("""What operation would you like to perform?
       1) Add 2) Subtract 3) Multiply 4) Divide""")
operation = input()

while operation not in ["1", "2", "3", "4"]:  #3 Add loop to validate operation input 
    prompt("You must choose 1, 2, 3, or 4")
    operation = input()

match operation:            #2:Replace if statement with match case statement
    case "1":               # '1' represents addition
        output = int(number1) + int(number2)
    case "2":               # '2' represents subtraction
        output = int(number1) - int(number2)
    case "3":               # '3' represents multiplication
        output = int(number1) * int(number2)
    case "4":
        output = int(number1) / int(number2)

prompt(f"The result is {output}")
