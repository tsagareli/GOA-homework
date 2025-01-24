# დაწერეთ პროგრამა, რომელიც დაბეჭდავს რიცხვებს 1-დან 10-მდე, თითო რიცხვს ახალ სტრიქონზე. გამოიყენეთ for ციკლი.
# დაწერეთ პროგრამა, რომელიც დაბეჭდავს ყველა ლუწ რიცხვს 1-დან 20-მდე. გამოიყენეთ for ციკლი და მოდულო ოპერატორი (%) ლუწი რიცხვების გასაგებად.
# დაწერეთ პროგრამა, რომელიც დაითვლის 10-დან 1-მდე უკან, თითო რიცხვს ახალ სტრიქონზე. გამოიყენეთ while ციკლი.
# დაწერეთ პროგრამა, რომელიც გენერირებს შემთხვევით რიცხვს 1-დან 10-მდე. მომხმარებელმა უნდა ამოიცნოს ეს რიცხვი. პროგრამამ უნდა განაგრძოს მოთხოვნა ახალი რიცხვის შეყვანის, სანამ მომხმარებელი სწორად არ ამოიცნობს რიცხვს. გამოიყენეთ while ციკლი ამოცნობის პროცესის განსახორციელებლად.
# დაწერეთ პროგრამა, რომელიც იღებს სტუდენტის ქულას შეყვანის სახით. ქულის მიხედვით დაბეჭდეთ შესაბამისი შეფასება:90-100:A,80-89: B,70-79: C,0-69: D,60-ზე ნაკლები: F,გამოიყენეთ if-elif-else პირობები შეფასების სისტემის განსახორციელებლად.
# დაწერეთ პროგრამა, რომელიც იღებს რიცხვს შეყვანის სახით და განსაზღვრავს, თუ არის ის ლუწი თუ კენტი. გამოიყენეთ if-else პირობა შესაბამისი შეტყობინების დასაბეჭდად.

for i in range(1, 11):
     print(i)

for i in range(1, 21):
      if i % 2 == 0:
       print(i)

i = 10
while i >= 1:
    print(i)
    i -= 1

import random
number = random.randint(1, 10)
while True:
     guess = int(input("Guess the number between 1 and 10: "))
     if guess == number:
         print("Congratulations! You've guessed the correct number.")
         break
     else:
         print("Incorrect guess. Try again!")

score = int(input("Enter the student's score: "))
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else:
    print("F")

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")