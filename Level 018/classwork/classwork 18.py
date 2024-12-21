def sort_list(numbers):

    for i in range(len(numbers)):
      if numbers[index] > numbers[index + 1]:
          numbers[index + 1] = numbers[index]


    return numbers




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