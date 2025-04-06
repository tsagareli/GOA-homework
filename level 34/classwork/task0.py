def multiply_numbers(num1, num2):
    return num1 * num2

result1 = multiply_numbers(2, 3)
result2 = multiply_numbers(4, 5)
result3 = multiply_numbers(6, 7)
result4 = multiply_numbers(8, 9)
result5 = multiply_numbers(10, 11)

print(f"2 * 3 = {result1}")
print(f"4 * 5 = {result2}")
print(f"6 * 7 = {result3}")
print(f"8 * 9 = {result4}")
print(f"10 * 11 = {result5}")




def sum_or_multiply(num1, num2):
    if num1 > 50:
        print(f"{num1} * {num2} = {num1 * num2}")
    else:
        print(f"{num1} + {num2} = {num1 + num2}")

sum_or_multiply(30, 20) 
sum_or_multiply(60, 5)  
sum_or_multiply(40, 10) 
