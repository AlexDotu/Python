The user enters the day of the week number (1-7) from the keyboard. It is necessary to display the names of the days of the week on the screen. For example, if 1, then the screen displays Monday, 2 - Tuesday, etc.
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
