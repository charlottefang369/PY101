# Q2
# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# def check_exclamation(my_string):
#     print(my_string.endswith('!'))

# check_exclamation(str1)
# check_exclamation(str2)


# Q3
# famous_words = "seven years ago..."
# append_phrase = "Four score and "
# # Solution #1:
# new_phrase = append_phrase + famous_words
# print(new_phrase)
# # Solution #2: 
# new_phrase = f'{append_phrase}{famous_words}'
# print(new_phrase)


# # Q4
# munsters_description = "the Munsters are CREEPY and Spooky."
# # => 'The munsters are creepy and spooky.'
# print(munsters_description.capitalize())


# Q5
# munsters_description = "The Munsters are creepy and spooky."
# print(munsters_description.swapcase())


#6
# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."
# target = 'Dino'
# print(target in str1)
# print(target in str2)


#7
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# print(flintstones)


#8 
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.extend(["Dino", 'Happy'])
# print(flintstones)


#9
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
print(advice[:advice.find('house')])


#10
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace('important', 'urgent'))