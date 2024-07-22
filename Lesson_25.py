# Task no.1 / The user enters three numbers from the keyboard. It is necessary to find the sum of the numbers, the product of the numbers. The result of the calculations is displayed on the screen./

number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
number3 = float(input('Enter third number: '))
sum = number1 + number2 + number3
multiplication = number1 * number2 * number3
print(sum,'\n', multiplication)

#==========

# Task no.2 /The user enters three numbers from the keyboard. The first number is the monthly salary, the second number is the monthly payment on a bank loan, and the third number is the debt for utilities. It is necessary to display the amount that the user will have left after all payments. /

number1 = float(input('Enter your salary: '))
number2 = float(input('Enter the amount of the loan's debt: '))
number3 = float(input('Enter the amount of debt for utilities: '))
print(number1 - (number2 + number3))

#==========

# Task no.3 /Write a program that calculates the area of ​​a rhombus. The user enters the length of its two diagonals from the keyboard./

number1 = float(input('Enter first diagonal: '))
number2 = float(input('Enter second diagonal: '))
print('The area of your rhombus is: ', (number1 * number2) / 2, 'm2')

#==========

# Task no.4 /Display the text "Life is what happens when you're busy making other plans" by John Lennon on different lines./

print("\"Life is what happens \n     when \n         you're busy making other plans\" \n                                     John Lennon")

#==========
