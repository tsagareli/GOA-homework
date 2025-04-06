def manual_capitalize(user_str):
    if len(user_str) > 0:
        return user_str[0].upper() + user_str[1:].lower()
    return user_str  

print(manual_capitalize("hello"))
print(manual_capitalize("WORLD"))
print(manual_capitalize("python"))
print(manual_capitalize("cOdIng"))
print(manual_capitalize("tEsT"))



def lower_or_upper(user_str, choice):
    if choice == "upper":
        print(user_str.upper())
    elif choice == "lower":
        print(user_str.lower())
    else:
        print("wrong choice")

lower_or_upper("hello", "upper")
lower_or_upper("WORLD", "lower")
lower_or_upper("Python", "mid") 
