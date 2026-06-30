import random 

import json 

with open ('rps_messages.json', 'r') as file:  
    MESSAGES = json.load(file)      #Assign MESSAGES with all the messages in rps_messages_json file.


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


def message(message_key):
    return MESSAGES[message_key]        #use message as key to look up messages in MESSAGE

def prompt(message):
    print(f'==> {message}')             #Prefix ==> to each message 

def display_welcome_message():
    prompt(message('welcome_1'))
    prompt(message('welcome_2'))

def display_goodbye_message():
    prompt(message('goodbye'))

def get_choice():
    while True:
        prompt(message('instruction')) 
        choice = input().lower().strip()
        if choice in VALID_CHOICES:
            return CHOICE_MAP[choice]

        prompt(message('invalid_choice')) 

def get_computer_choice():
    return CHOICE_MAP[random.choice(VALID_CHOICES)]

def player_wins(player, computer):
    return computer in WINNING_COMBOS[player]

def display_winner(player, computer):
    if player_wins(player, computer):
        prompt(message('win_user')) 
    elif player == computer: 
        prompt(message('tie')) 
    else: 
        prompt(message('win_computer')) 

def play_again():
    while True:
        prompt(message('play_again')) 
        answer = input().lower().strip()
        
        if answer and answer[0] in ['y', 'n']:
            return answer[0] == 'y'
        
        prompt(message('invalid_answer')) 

def play_rps():
   
    display_welcome_message()

    user_scores = 0
    computer_scores = 0

    while True:
        player = get_choice()
        computer = get_computer_choice()

        prompt(message('choices').format(player=player, computer=computer)) 

        if player_wins(player, computer):
            user_scores += 1
        elif player != computer:
            computer_scores += 1

        display_winner(player, computer)

        prompt(message('scores').format(user_scores=user_scores, computer_scores=computer_scores))

        if user_scores == 3:
            prompt(message('grand_winner_user'))
        elif computer_scores == 3:
            prompt(message('grand_winner_computer'))
        
        if user_scores == 3 or computer_scores == 3:
            if play_again():
                user_scores = 0
                computer_scores = 0
                display_welcome_message()
            else:
                display_goodbye_message()
                break

play_rps()



    

    