# Task 1: Reading a File
  # 1. Write a program that asks the user for the name of a file to read.
  # 2. Try to open and read the contents of the file.
  # 3. If the file does not exist, the program should handle the error and print the message "File not found."

def read_file():
    filename = input("Введите имя файла для чтения: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Содержимое файла:")
            print(content)
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


read_file()
#=====================
# # Task 2: Square Root
  # 1. Write a program that asks the user for a number.
  # 2. Try to calculate the square root of this number.
  # 3. Handle a possible error (for example, if the user enters a negative number) and print the message "The square root of a negative number is not defined."
import math

try:
    number = float(input("Введите Ваше число: "))

    if number < 0:
        raise ValueError("Квадратный корень из отрицательного числа не определен.")

    sqrt_result = math.sqrt(number)
    print(f"Квадратный корень из {number} равен {sqrt_result}")

except ValueError as e:
    print(e)
except Exception as e:
    print(f"Произошла ошибка: {e}")

#=====================
# #Task 3: Converting to a List
  # 1. Write a program that asks the user for a string of numbers separated by commas (for example, "1,2,3,4,5").
  # 2. Try to convert this string into a list of numbers.
  # 3. Handle possible errors (for example, if the user enters something that cannot be converted to a number) and display the message "Invalid input, try again."
string_of_numbers = input("Enter the string of numbers: ")
try:
    numbers = [float(num.strip()) for num in string_of_numbers.split(',')]
    print(f"The converted list of numbers is: {numbers}")
except ValueError:
    print("Invalid input, please try again")

#=====================
# Task 4: Division with type conversion
  # 1. Write a program that asks the user for two numbers.
  # 2. Try to divide these numbers by converting them from strings to numbers.
  # 3. Handle possible errors, such as division by zero or entering an invalid number (for example, a string that cannot be converted to a number).
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
try:
    division1 = int(number1) / int(number2)
    division2 = int(number2) / int(number1)
    print(f'Dividing the first number by the second equals: {division1}')
    print(f'Dividing the second number by the first equals: {division2}')

except ValueError:
    print("Invalid input, please try again")
except ZeroDivisionError:
    print("ATTENTION ! Division of numbers by zero is impossible")

#=====================
# Task 5: Handling multiple exceptions
  # 1. Write a program that asks the user for two numbers and an operation (+, -, *, /).
  # 2. Try to perform the selected operation.
  # 3. Handle several possible exceptions: division by zero, invalid number input, invalid operation symbol, and display the appropriate messages.
try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    sign = input("Enter the sign: ")
    if sign == "+":
        print(f"result: {number1 + number2}")
    elif sign == "-":
        print(f"result: {number1 - number2}")
    elif sign == "*":
        print(f"result: {number1 * number2}")
    elif sign == "/":
        if number2 == 0:
            raise ZeroDivisionError
        print(f"result: {number1 / number2}")
    else:
        print("Invalid operation sign. Please enter one of the characters: +, -, *, /.")
except ZeroDivisionError as e:
    print("ATTENTION ! Division of numbers by zero is impossible. Please enter another number!")
except ValueError as e:
    print("Invalid input, please try again")

#=====================
# Task 6: Multiple input errors
  # 1. Write a program that asks the user for three numbers.
  # 2. Try to find their average value.
  # 3. Handle possible errors, such as incorrect entry of any of the numbers, and display a message indicating which number was entered incorrectly.

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


numbers = []
for i in range(1, 4):
    user_input = input(f"Enter the number {i}: ")
    if is_number(user_input):
        numbers.append(float(user_input))
    else:
        print(f"Error: Invalid value entered for number {i}: '{user_input}'")
        break
else:
    average = sum(numbers) / len(numbers)
    print(average)
#=====================
