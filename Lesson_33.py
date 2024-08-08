# Task 1 / Write a function that calculates the product of the elements of a list of integers. The list is passed as a parameter. The result obtained is returned from the function./ #

def multiply(spisok):         

    result = 1                
    for number in spisok:     
        if number % 1 == 0 and number != 0:   
            result *= number  
    print(result)             
    return result                                                                    
                                                                                  
spisok = [-1, 0, 1, 2, -2, 3, 4, 5, -5, 6, 7, 8, 9, 10, 11, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9] 
print(f'Your result is: ', end="")  
multiply(spisok)                                      

# Task 2 / Write a function to find the minimum in a list of integers. The list is passed as a parameter. The obtained result is returned from the function./
def minimum(spisok):
    mini = min(spisok)
    for el in spisok:
        if el % 1 == 0:
            print(f'Your minimal number is: ', mini)
            return mini

minimum(spisok = [-1, 0, 1, 2, -2, 3 -3, -1, 4, 5, -5, 6, 7, 8, 9, 10, -11, 1.1, 2.2, 3.3, 4.4, 5.5, -6.6, 7.7, 8.8, 9.9])


# Task 3 / Write a function that determines the number of prime numbers in a list of integers. The list is passed as a parameter. The result obtained is returned from the function./
def func(list):
    list2 = []
    for i in list:
        if i % 1 == 0:
            if i > 1 and (i % 2 != 0 or i == 2) and (i % 3 != 0 or i == 3):
                list2.append(i)
    print(len(list2))


func(list=[-1, 0, 1, 2, -2, 3, 4, 5, -5, 6, 7, 8, 9, 10, 11, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])


# Task 4 / Write a function that removes a given number from a list of integers. The function must return the number of removed elements./
def remove_and_count(my_list, number_to_delete):
    count: int = 0
    for i in my_list:
        if i == number_to_delete:
            my_list.remove(i)
            count += 1
    return count


my_list = [-1, 0, 1, 2, -2, 3, 4, 5, -5, 6, 7, 8, 9, 10, 11, 5, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
number_to_delete = float(input("Enter the number witch should be deleted: "))
final_number = remove_and_count(my_list, number_to_delete)
print(f'Number of deleted numbers: ', final_number)

# Task 5 / Write a function that receives two lists as a parameter and returns a list containing the elements of both lists./ 
def sum_of_lists(list1, list2):
    list3 = list1 + list2
    print(list3)
    return list3


list1 = ['A', 1, 2, 3, 4, 5]
list2 = ['B', 6, 7, 8, 9, 0]
sum_of_lists(list1, list2)

# Task 6 / Write a function that calculates the degree of each element of a list of integers. The value for the degree is passed as a parameter, and the list is also passed as a parameter. The function returns a new list containing the results obtained./
def degree_of_the_number(list, degree):
    list2 = []
    for n in list:
        if degree < 0 and n == 0:
            print(
                'Тк \"Ноль\" нельзя возводить в отрицательную степень, то ниже указаны результаты возведения, кроме \"Нуля\":')
        elif n % 1 == 0:
            n2 = n ** degree

            list2.append(n2)
    print(list2)
    return list2


list = [-1, 0, 1, 2, -2, 3, 4, 5, -5, 6, 7, 8, 9, 10, 11, 5, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
degree = float(input("Enter the desired degree for the numbers: "))
degree_of_the_number(list, degree)
