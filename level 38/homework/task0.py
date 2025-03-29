# Islower

# 2) Check if all characters in a given string are lowercase and print the result.
# 2) Create a function that takes a string and returns True if it is completely in lowercase, otherwise False.
# 3) Prompt the user to input a string and verify if it contains only lowercase letters.

# Isupper

# 4) Verify if all the characters in a user-provided string are uppercase.
# 5) Write a function that checks if a string consists entirely of uppercase letters and returns a boolean result.
# 6) Check and display whether a string input by the user is in uppercase.

# Swapcase

# 7) Convert a string such that uppercase letters become lowercase and vice versa, then print the result.
# 8) Write a function that takes a sentence and returns it with swapped case for each letter.

# 9) Write a function that takes a user's name and age, and returns a welcome message formatted with an f-string.
# 10) Write a function that takes a sentence and returns a list of words.

#2
text = input("Enter a string: ")
if text.islower():
    print("All characters are lowercase.")
else:
    print("Not all characters are lowercase.")

#3
def is_lowercase(text):
    return text.islower()

print(is_lowercase("hello")) 
print(is_lowercase("Hello"))  

#4
user_input = input("Enter a string: ")
if user_input.islower():
    print("The string contains only lowercase letters.")
else:
    print("The string does not contain only lowercase letters.")

#5
user_input = input("Enter a string: ")
if user_input.isupper():
    print("All characters are uppercase.")
else:
    print("Not all characters are uppercase.")

#6
def is_uppercase(text):
    return text.isupper()

print(is_uppercase("HELLO"))  
print(is_uppercase("Hello"))  

#7
user_input = input("Enter a string: ")
if user_input.isupper():
    print("The string is in uppercase.")
else:
    print("The string is not in uppercase.")

#8
text = input("Enter a string: ")
swapped_text = text.swapcase()
print("Swapped case:", swapped_text)

#9
def swap_case(sentence):
    return sentence.swapcase()

print(swap_case("Hello World!"))  

#10
def welcome_message(name, age):
    return f"Welcome {name}, you are {age} years old!"

print(welcome_message("Alice", 30))  

#11
def sentence_to_words(sentence):
    return sentence.split()

print(sentence_to_words("Hello World from Python"))  