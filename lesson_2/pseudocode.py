# Exercise #1: a function that returns the sum of two numbers

# Casual: 
# Given two numbers.
# Add the first number to the second number.
# Return the result.

# Formal: 
# START

# # Given two numbers: number1 and number2

# SET sum = number1 + number2

# PRINT sum

# END





# Exercise #2: a function that takes a list of strings, and returns a string 
# that is all those strings concatenated together

# Casual:
# Given a list of strings.
# Start with an empty result string.
# For each string in the list, add it to the result string.
# Return the result string.

# Formal: 
# START

# Given a list of strings called strings

# SET result = empty string
# SET iterator = 0

# WHILE iterator < length of strings
#     SET current_string = value within strings at position iterator
#     SET result = result + current_string
#     SET iterator = iterator + 1

# PRINT result

# END





# Exercise #3: a function that takes a list of integers, and returns a new list 
# with every other element from the original list, starting with the first 
# element. 

# Casual:
# Given a list of integers
# Start with an empty result list.
# Starting from the first element in the original list, if the index of the 
# integer is even, add it to the result list; if the index is odd, skip it. 
# Return the result list.

# Formal: 
# START 

# Given a list of integers called numbers 

# SET result = empty list
# SET iterator = 0

# WHILE iterator < length of numbers
#     IF iterator is even:
#         SET current_number = value within numbers at position iterator
#         append current_number to result

#     SET iterator = iterator + 1

# PRINT result

# END





# Exercise #4: a function that determines the index of the 3rd occurrence of a 
# given character in a string. For instance, if the given character is 'x' and 
# the string is 'axbxcdxex', the function should return 6 (the index of the 
# 3rd 'x'). If the given character does not occur at least 3 times, return 
# None.

# Casual:
# Given a string and a character.
# Start with the first character of the string from left and compare each 
# character of the string to the given character. 
# Track and count the number of the time matched. 
# When the count reaches 3, return the index of the current character
# If that total number is less than 3, return None 

# Formal: 
# START 

# Given a string called my_string and a character called char.

# SET count = 0
# SET iterator = 0 

# WHILE iterator < length of my_string: 
#     SET current_char = value within my_string at position iterator

#     IF current_char is equal to char:
#         SET count = count + 1

#         IF count is equal to 3:
#             PRINT iterator 
#     
#     SET iterator = iterator + 1

# PRINT None

# END



# Exercise #5:a function that takes two lists of numbers and returns the result 
# of merging the lists. The elements of the first list should become the 
# elements at the even indexes of the returned list, while the elements of the 
# second list should become the elements at the odd indexes. 

# Casual:
# Given two lists of numbers: list1 and list2.
# Start with an empty list called result. 
# Add the first element of list1 to result and add the frist element of list2 
# to the result. Then add the second element of list1 to result and add the
# second element of list2 to the result. Continue this process until exhaust 
# both list1 and list2. 
# Return the result list. 

# Formal: 
# START 

# Given two lists of numbers: list1 and list2.

# SET result = empty list
# SET iterator = 0

# WHILE iterator < length of the list1
#     SET current_number1 = value within list1 at position iterator
#     append current_number1 to result

#     SET current_number2 = value within list2 at position iterator
#     append current_number2 to result
# 
#     SET iterator = iterator + 1

# PRINT result 

# END