def print_arr(lst):
    for item in lst:
        print(item)

my_list = [1, 2, 3, 4, 5]
print_arr(my_list)


def check(s):
    return 4 < len(s) < 8

print(check("hello"))   
print(check("hi"))      
print(check("elephant")) 

def no_spaces(s):
    return s.replace(" ", "-")

print(no_spaces("hello world"))   
print(no_spaces("Python is fun")) 
print(no_spaces(" no spaces "))   


def Is_best_academy():
    print("Goal-Oriented-Academy")

Is_best_academy()


def complex_calc(a, b):
    if a % 2 == 0:  
        return a + b
    else: 
        return a * b

print(complex_calc(4, 5))  
print(complex_calc(3, 5))  
print(complex_calc(10, 2)) 
print(complex_calc(7, 3)) 


def BONUS(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    
    lst.reverse()
    
    lst = odd_numbers + lst
    
    return lst

print(BONUS([1, 2, 3, 4, 5, 6, 7]))  
print(BONUS([10, 9, 8, 7, 6, 5]))    