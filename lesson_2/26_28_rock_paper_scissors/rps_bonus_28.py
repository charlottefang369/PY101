import random 

VALID_CHOICES = ['r', 'p', 'sc', 'l', 'sp']

VALID_CHOICES_DETAIL = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'rock' and computer == 'lizard') or
        (player == 'paper' and computer == 'spock') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'scissors' and computer == 'lizard') or
        (player == 'spock' and computer == 'scissors') or
        (player == 'spock' and computer == 'rock') or
        (player == 'lizard' and computer == 'spock') or
        (player == 'lizard' and computer == 'paper')):
        prompt ('You win!')
    elif player == computer: 
        prompt ('It is a tie!')
    else: 
        prompt ('Computer wins!')

user_scores = 0
computer_scores = 0

while True:
    while True: 
        prompt('Choose one: "r" for rock, "p" for paper,'
               '"sc" for scissors,"l" for lizard, "sp" for spock')
        choice = input()
        
        if choice in VALID_CHOICES:
            break 

        prompt("That is not a valid player")
    
    computer_choice = random.choice(VALID_CHOICES)

    for valid_choice in VALID_CHOICES_DETAIL: 
        if valid_choice.startswith(choice):
            choice = valid_choice 
        if valid_choice.startswith(computer_choice):
            computer_choice = valid_choice 

    prompt(f'You chose {choice}, computer chose {computer_choice}')
  
    display_winner(choice, computer_choice)

    if ((choice == 'rock' and computer_choice == 'scissors') or
        (choice == 'rock' and computer_choice == 'lizard') or
        (choice == 'paper' and computer_choice == 'spock') or
        (choice == 'paper' and computer_choice == 'rock') or
        (choice == 'scissors' and computer_choice == 'paper') or
        (choice == 'scissors' and computer_choice == 'lizard') or
        (choice == 'spock' and computer_choice == 'scissors') or
        (choice == 'spock' and computer_choice == 'rock') or
        (choice == 'lizard' and computer_choice == 'spock') or
        (choice == 'lizard' and computer_choice == 'paper')):
        user_scores = user_scores + 1
    elif choice == computer_choice: 
        pass
    else: 
        computer_scores = computer_scores +1
    
    if user_scores == 3:
        prompt('You are the grand winner!')
    elif computer_scores == 3:
        prompt('Computer is the grand winner!')


    #Allow Y/N, y/n, Yes/No, YES/NO
    while True: 
        prompt ('Do you want to play again (y/n)?')
        answer = input().lower()

        #Using and operator's short circuit behavior to fliter out empty string 
        if answer and answer[0] in ['y', 'n']:  
            break 

        prompt('Please enter "y" or "n".')
    
    #Break if the user doesn't want to play again 
    if answer[0] == 'n':
        break 
    