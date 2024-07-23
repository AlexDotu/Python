# Task no.1 / The user enters a two-digit number from the keyboard. For example, 26. It is necessary to show the value of the first and second digits on different lines. In our case, it will look like this:
#2
#6/

number = input("Enter your number: ")
first_digit = number[0]
second_digit = number[1]
print(first_digit)
print(second_digit)

#==========

# Task no.2 /The user enters a three-digit number from the keyboard. For example, 891. You need to show the value of the first, second, and third digits on different lines. You also need to show the sum of these three numbers on a separate line. In our case, it will look like this:
#8
#9
#1
#18 / 

number = input("Enter your number: ")
first_digit = number[0]
second_digit = number[1]
third_digit = number[2]
print(first_digit)
print(second_digit)
print(third_digit)
print(int(first_digit) + int(second_digit) + int(third_digit))

#==========

# Task no.3 /The user enters two digits from the keyboard. It is necessary to create a number containing these digits. For example, Practical task 1 if 9, 7 are entered from the keyboard, then the number 97 must be formed / 

a = int(input("write 1st number: "))
b = int(input("write 2nd number: "))
print(f'{a}{b}')

#==========


# Task no.4 /The user enters the temperature on the Celsius scale from the keyboard. The temperature must be converted to Fahrenheit and displayed on the screen. /

number = float(input("Enter temperature in Celsius degrees: "))
print('Temperature in Fahrenheit is:', 32+number*1.8)

#==========
