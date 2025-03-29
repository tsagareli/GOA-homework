# Upper
# 2) Convert a given sentence to uppercase and print the result.
# 3) Take a user's name input and display it in uppercase letters.
# 4) Create a function that converts a list of lowercase strings to uppercase.

# Lower
# 5) Convert all the characters of a given sentence to lowercase and print it.
# 6) Ask the user for their email address and ensure it is stored in lowercase.
# 7) Write a function that takes a mixed-case string and returns it in all lowercase letters.

# Capitalize
# 8) Capitalize the first letter of a sentence provided by the user.
# 9) Given a list of lowercase strings, capitalize the first letter of each string.
# 10) Create a function that takes a string and returns it with the first letter capitalized.

# Find
# 11) Find the position of the first occurrence of the word "Python" in a sentence.
# 12) Search for a user-specified substring in a provided string and print its starting index.
# 13) Write a function to find and return the index of a specified character in a given string.

# Len
# 14) Find and print the length of a user-provided string.
# 15) Write a function that takes a list of strings and returns their lengths.

# Count
# 16) Count the number of times the word "the" appears in a given paragraph.
# 17) Ask the user to input a character and count its occurrences in a given string.
# 18) Create a function that counts and returns the occurrences of a specified word in a text.

#2
sentence = input("Enter a sentence: ")
print(sentence.upper())

#3
name = input("Enter your name: ")
print(name.upper())

#4
def convert_to_uppercase(string_list):
    return [s.upper() for s in string_list]

print(convert_to_uppercase(["hello", "world", "python"]))  

#5
sentence = input("Enter a sentence: ")
print(sentence.lower())

#6
email = input("Enter your email address: ")
email = email.lower()
print(f"Your email in lowercase is: {email}")

#7
def to_lowercase(text):
    return text.lower()

print(to_lowercase("Hello World!"))  

#8
sentence = input("Enter a sentence: ")
print(sentence.capitalize())

#9
def capitalize_first_letter(strings):
    return [s.capitalize() for s in strings]

print(capitalize_first_letter(["hello", "world", "python"]))  

#10
def capitalize_first_char(text):
    return text.capitalize()

print(capitalize_first_char("hello world")) 

#11
sentence = input("Enter a sentence: ")
position = sentence.find("Python")
if position != -1:
    print(f"The word 'Python' is first found at position: {position}")
else:
    print("The word 'Python' is not found.")

#12
text = input("Enter a string: ")
substring = input("Enter the substring to search for: ")
index = text.find(substring)
if index != -1:
    print(f"The substring is found at index: {index}")
else:
    print("Substring not found.")

#13
def find_char_index(text, char):
    return text.find(char)

print(find_char_index("Hello, world!", "o"))  

#14
text = input("Enter a string: ")
print(f"The length of the string is: {len(text)}")

#15
def get_string_lengths(strings):
    return [len(s) for s in strings]

print(get_string_lengths(["apple", "banana", "cherry"]))  

#16
paragraph = input("Enter a paragraph: ")
count = paragraph.lower().split().count("the")
print(f"The word 'the' appears {count} times.")

#17
text = input("Enter a string: ")
char = input("Enter a character to count: ")
count = text.count(char)
print(f"The character '{char}' appears {count} times in the string.")

#18
def count_word_occurrences(text, word):
    return text.lower().split().count(word)

print(count_word_occurrences("the quick brown fox jumps over the lazy dog", "the"))  