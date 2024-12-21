def sum_of_numbers(numbers):
    result = 0 
    for i in numbers:
        result += i
    return result


numbers = [1, 2, 3, 4, 5]   
print(sum_of_numbers(numbers))


def filter(strings_list):
    filtered_list = []

    for word in strings_list:
        if len (word) > 5: 
            filtered_list.append(word)

    return filtered_list


names = ["Nika","Luka","Gabrieli","Dato","Giorgi"]

print(filter(names))


def even_numbers(numbers):
    even_numbers_list = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers_list.append(num)
    return even_numbers_list

print(even_numbers([1,2,3,4,5,6,7,8,9,10]))




def largest_number(numbers):
    max_number = numbers[0]
    for num in numbers:
        if max_number < num:
            max_number = num
 
    return max_number
    
numbers = [4,3,5,2,1 ]

print(largest_number())

def filter_even(numbers):
    filtered_list = [] 

    for num in numbers:
        if num > 10 and num % 2 ==0: 
            filtered_list.append(num)

def sum_of_numbers(numbers):
    sum = 0 

    for i in numbers :
        sum = sum + i 


count = int(input("please enter how many numbers do you want to input: "))

numers = []

for i in range(count):
    num = int(input("please enter number: "))
    numbers.append(num)
            

print(sum_of_numbers(numbers))
print(filter_even(numbers))





