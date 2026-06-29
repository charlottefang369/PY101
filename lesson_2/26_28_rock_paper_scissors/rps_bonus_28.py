import random 

VALID_CHOICES = ['r', 'p', 'sc', 'l', 'sp']

CHOICE_MAP = {
    'r':  'rock',
    'p':  'paper',
    'sc': 'scissors',
    'l':  'lizard',
    'sp': 'spock',
}

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def prompt(message):
    print(f'==> {message}')

def display_welcome_message():
    prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
    prompt('First to 3 wins takes the match. Good luck!')

def display_goodbye_message():
    prompt('Thanks for playing. Goodbye!')

def get_choice():
    while True:
        prompt('Choose one: '
               '"r" for rock, "p" for paper, "sc" for scissors, "l" for lizard, "sp" for spock') 
        choice = input().lower().strip()
        if choice in VALID_CHOICES:
            return CHOICE_MAP[choice]

        prompt("That is not a valid choice")

def get_computer_choice():
    return CHOICE_MAP[random.choice(VALID_CHOICES)]

def player_wins(player, computer):
    return computer in WINNING_COMBOS[player]

def display_winner(player, computer):
    if player_wins(player, computer):
        prompt('You win!')
    elif player == computer: 
        prompt('It is a tie!')
    else: 
        prompt('Computer wins!')

def play_again():
    while True:
        prompt('Do you want to restart the game (y/n)?')
        answer = input().lower().strip()
        
        if answer and answer[0] in ['y', 'n']:
            return answer[0] == 'y'
        
        prompt('Please enter "y" or "n".')

def play_rps():
    user_scores = 0
    computer_scores = 0
   
    display_welcome_message()

    while True:
        player = get_choice()
        computer = get_computer_choice()

        prompt(f'You chose {player}, computer chose {computer}')

        display_winner(player, computer)

        if player_wins(player, computer):
            user_scores += 1
        elif player != computer:
            computer_scores += 1

        prompt(f'Score - You: {user_scores} | Computer: {computer_scores}')

        if user_scores == 3:
            prompt('You are the grand winner!')
        elif computer_scores == 3:
            prompt('Computer is the grand winner!')
        
        if user_scores == 3 or computer_scores == 3:
            if play_again():
                user_scores = 0
                computer_scores = 0
                display_welcome_message()
            else:
                display_goodbye_message()
                break

play_rps()



    

    