def big_sentence(name, surname, age, color):
    print(f"My name is {name} {surname}, I am {age} years old, and my favorite color is {color}.")

big_sentence("John", "Doe", 25, "blue")


def check_lowercase(user_str):
    if user_str.islower():
        print("The string is all lowercase.")
    else:
        print("The string is not all lowercase.")

check_lowercase("hello")
check_lowercase("Hello")
check_lowercase("WORLD")


def list_join(user_list, str_to_join):
    print(str_to_join.join(user_list))

list_join(["apple", "banana", "cherry"], ", ")
list_join(["hello", "world"], "-")
list_join(["2025", "02", "09"], "/")


def element_remover(user_list, index_to_remove):
    del user_list[index_to_remove]

list1 = [1, 2, 3, 4, 5]
element_remover(list1, 2) 
print(list1)  

list2 = ['a', 'b', 'c', 'd']
element_remover(list2, 0) 
print(list2)  

list3 = [True, False, True, False]
element_remover(list3, 1)  
print(list3)  