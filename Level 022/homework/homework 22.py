 
# 8kyu

# get character from ASCII Value

def get_char(c):
  return chr(c)


#Find the Difference in Age between Oldest and Youngest Family Members
def difference_in_ages(ages):
    # your code here
    youngest_age = min(ages)
    oldest_age = max(ages)
    difference = oldest_age - youngest_age
    return (youngest_age, oldest_age, difference)



# Find the smallest integer in the array
def find_smallest_int(arr):
    smallest = arr[0] 
    
    for num in arr:
        if smallest > num:
            smallest = num
            
    return smallest



# 2)
def find_smallest_int(arr):
    min = arr[0]
    for item in arr:
        if min > item:
            min = item
    return min

#Multiply
def multiply(a, b):
    return a * b

# Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2
# 8kyu end


# 7 kyu start

# Binary Addition

def add_binary(a,b):
    return bin(a+b) [2:]


# List Filtering
def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list


# Descending Order
def descending_order(num):
      return int("".join(sorted(str(num),reverse=True)))
   