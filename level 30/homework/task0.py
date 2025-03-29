# 2) თქვენი სიტყვებით ახსენით რა არის list, indexing. ახსენით როგორ მუშაობს indexing
# 3) Create a list of five numbers and print the first, third, and last elements using indexing.
# 4) Create a list of 20 elements (any data type) and print all of the elements - use indexing
# 5) Create list of 5 elements and then change all of them, using indexing

#2
#List არის ელემენტების სერია, რომელიც შეიძლება შეიცავდეს სხვადასხვა ტიპის მონაცემებს. Indexing ნიშნავს, რომ ლისტში თითოეული ელემენტს აქვს უნიკალური ინდექსი, რომელიც იწყება 0-დან.

#3
numbers = [10, 20, 30, 40, 50]
print(numbers[0], numbers[2], numbers[-1])

#4
elements = [1, "apple", 3.14, True, "hello", 42, 99, "world", 88, 7.5, "python", False, 100, "list", "example", 55, 77, 12, "end", 21]
for i in range(len(elements)):
    print(elements[i])

#5
my_list = [5, "apple", 3.14, True, "hello"]
my_list[0] = 10
my_list[1] = "orange"
my_list[2] = 2.71
my_list[3] = False
my_list[4] = "world"
print(my_list)