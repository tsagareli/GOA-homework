def find_min_with_min_function(lst):
    return min(lst)

def find_min_with_algorithm(lst):
    min_value = lst[0]  
    for num in lst[1:]:  
        if num < min_value:  
            min_value = num
    return min_value

example_list = [10, 3, 5, 1, 9]

min_value_with_min = find_min_with_min_function(example_list)
min_value_with_algorithm = find_min_with_algorithm(example_list)

print(f"min() ფუნქციით მინიმუმი: {min_value_with_min}")
print(f"ალგორითმით მინიმუმი: {min_value_with_algorithm}")
