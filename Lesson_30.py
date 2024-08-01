# Task no.1 /The user enters the day of the week number (1-7) from the keyboard. 
#It is necessary to display the names of the days of the week on the screen. For example, if 1, then the screen displays Monday, 2 - Tuesday, etc./

number = int(input("Enter the number of the day: "))
day_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
while 1 <= number <= 7:
    if number == 1:
        print(day_of_the_week[0])
        break
    if number == 2:
        print(day_of_the_week[1])
        break
    if number == 3:
        print(day_of_the_week[2])
        break
    if number == 4:
        print(day_of_the_week[3])
        break
    if number == 5:
        print(day_of_the_week[4])
        break
    if number == 6:
        print(day_of_the_week[5])
        break
    if number == 7:
        print(day_of_the_week[6])
        break
else:
    print('Please enter a valid number of the week')


# Task no.2 /The user enters the month number (1-12) from the keyboard. The name of the month must be displayed on the screen. For example, if 1, then the text on the screen is January, 2 - February, etc. /

number = int(input("Enter the month number (1-12) from the keyboard: "))
month_of_the_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while 1 <= number <= 12:
    if number == 1:
        print(month_of_the_year[0])
        break
    if number == 2:
        print(month_of_the_year[1])
        break
    if number == 3:
        print(month_of_the_year[2])
        break
    if number == 4:
        print(month_of_the_year[3])
        break
    if number == 5:
        print(month_of_the_year[4])
        break
    if number == 6:
        print(month_of_the_year[5])
        break
    if number == 7:
        print(month_of_the_year[6])
        break
    if number == 8:
        print(month_of_the_year[7])
        break
    if number == 9:
        print(month_of_the_year[8])
        break
    if number == 10:
        print(month_of_the_year[9])
        break
    if number == 11:
        print(month_of_the_year[10])
        break
    if number == 12:
        print(month_of_the_year[11])
        break
else:
    print("Enter a valid month number!")

# Task no.3 / The user enters a number from the keyboard. If the number is greater than zero, the message "Number is positive" should be displayed, if less than zero "Number is negative", if equal to zero "Number is equal to zero" /

number = int(input("Enter your number: "))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
elif number == 0:
    print("Number is equal zero")
else:
    print("Enter a valid number !!!")

# Task no.4 / The user enters two numbers. Determine whether these numbers are equal, and if not, display them on the screen in ascending order./

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
if number1 == number2:
    print("First number is equal to second number!")
elif number2 > number1:
    print(number1, number2)
elif number1 > number2:
    print(number2, number1)
else:
    print("Please enter a valid number!!!")

#Task 5 / The user enters a six-digit integer from the keyboard. Write a program that determines whether the entered number is lucky (A six-digit number is considered lucky if the sum of the first three digits is equal to the sum of the second three digits). For example, 123321 is a lucky number, since 1+2+3 = 3+2+1. On the other hand, 378423 is an unlucky number, since 3+7+8 != 4+2+3. If the user has not entered a six-digit number, an error message must be displayed.

number = input("Enter your number: ")
while len(number) == 6:
    if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
        print("This is a lucky number !!!")
        break
    elif int(number[0]) + int(number[1]) + int(number[2]) != int(number[3]) + int(number[4]) + int(number[5]):
        print("This is NOT a lucky number !")
        break
else:
    print("Please enter a valid 6 digit number !")
