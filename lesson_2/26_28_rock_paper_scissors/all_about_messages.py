#ALL ABOUT MESSAGES 

import json 

with open ('rps_messages.json', 'r') as file:  
    MESSAGES = json.load(file)      # Assign MESSAGES with all the messages in rps_messages_json file.

def message(message_key):
    return MESSAGES[message_key]    # use message as key to look up messages in MESSAGE

def prompt(message):
    print(f'==> {message}')         # Prefix ==> to each message 





def display_welcome_message():
    prompt(message('welcome_1'))
    prompt(message('welcome_2'))

def display_goodbye_message():
    prompt(message('goodbye'))

prompt(message('instruction')) 
prompt(message('invalid_choice')) 
prompt(message('win_user')) 
prompt(message('tie')) 
prompt(message('win_computer')) 
prompt(message('play_again')) 
prompt(message('invalid_answer')) 




# When detailed message is a f'string, 
# use method call .format() and keyword arguments for {variable/expression}
prompt(message('choices').format(player=player, computer=computer))
prompt(message('scores').format(user_scores=user_scores, computer_scores=computer_scores))




