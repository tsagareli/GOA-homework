# 2) თქვენი სიტყვებით ახსენით რა არის slicing და რაში ვიყენებთ მას
# 3) Get the first element from a list.
# 4) Get the last element from a list using negative indexing.
# 5) Slice the first three elements of a list.
# 6) Get the last five elements from a string.

#2
#Slicing არის პროცესი, როდესაც ვყოფთ მონაცემთა სტრუქტურას გარკვეული მოცულობის მიხედვით. მაგალითად, Python-ში, თუ გვინდა კონკრეტული ნაწილის ამოღება სიის ან სტრიქონისგან, ვიყენებთ slicing-ს.

#3
my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]  
print(first_element)

#4
my_list = [10, 20, 30, 40, 50]
last_element = my_list[-1]  
print(last_element)

#5
my_list = [10, 20, 30, 40, 50]
first_three_elements = my_list[:3]  
print(first_three_elements)

#6
my_string = "Hello, world!"
last_five_chars = my_string[-5:]  
print(last_five_chars)