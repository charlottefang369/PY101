import random 

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
choice = input()

while choice not in VALID_CHOICES:
    prompt("That is not a valid choice")
    choice = input()

# while True: 
#     prompt('Choose one: rock, paper, scissors')
#     choice = input()
    
#     if choice in VALID_CHOICES:
#         break 

#     prompt("That is not a valid choice")


computer_choice = random.choice(VALID_CHOICES)

prompt(f'You chose {choice}, computer chose {computer_choice}')