def sum_two_smallest_numbers(numbers):
    minmum1 = min(numbers)
    numbers.remove(minmum1)
    minmum2 = min(numbers)
    
    return minmum1 + minmum2