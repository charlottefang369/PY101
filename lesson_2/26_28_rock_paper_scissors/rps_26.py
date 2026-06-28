import random 

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')):
        prompt ('You win!')
    elif player == computer: 
        prompt ('It is a tie!')
    else: 
        prompt ('Computer wins!')

while True:
    while True: 
        prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
        choice = input()
        
        if choice in VALID_CHOICES:
            break 

        prompt("That is not a valid player")


    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}')
  
    display_winner(choice, computer_choice)
    

    #Allow Y/N, y/n, Yes/No, YES/NO
    while True: 
        prompt ('Do you want to play again (y/n)?')
        answer = input().lower()

        if answer and answer[0] in ['y', 'n']:  #Using and operator's short circuit behavior to fliter out empty string 
            break 

        prompt('Please enter "y" or "n".')
    
    #Break if the user doesn't want to play again 
    if answer[0] == 'n':
        break 
    