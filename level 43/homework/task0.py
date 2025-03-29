# 1) შექმენით ფუნქცია რომელიც არგუმენტად იღებს ლისთს და აბრუნებს მის პირველ და ბოლო ელემენტს ლისთში.  
# 2) შექმენით ფუნქცია რომელიც გადაეცემა სამი ინტჯერი და აბურნებს უდიდეს.
# 3) შექმენით ფუნქცია რომელიც იღებს სტრინგს არგუმენტად და აბრუნებს მას შეტრიალებულს.
# BONUS: ეცადეთ გააკეთოთ მესამე დავალება სტრინგ სლაისინგის გარეშე.

#1
def get_first_and_last(lst):
    return [lst[0], lst[-1]]

#2
def get_largest(a, b, c):
    return max(a, b, c)

#3
def reverse_string(s):
    return s[::-1]

#bonus
def reverse_string_without_slicing(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str