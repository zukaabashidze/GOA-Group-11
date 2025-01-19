#Break CamelCase 
def solution(s):
    result = ''
    for char in s:
        if char.isupper() and result != '':
            result += ' ' + char
        else:
            result += char

    return result
# Make Funciton That does arithmetic
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        if b == 0:
            return "cannot divide by zero"
        return a / b
    else:
        return "invalid operator"


# Number of People in the bus 
def number(bus_stops):
    total_people = 0
    for stop in bus_stops:
        people_get_on, people_get_off = stop
        total_people += people_get_on - people_get_off
    return total_people if total_people >= 0 else 0

# Pyramid Array 
def pyramid(n):
    return [[1] * (i + 1) for i in range(n)]