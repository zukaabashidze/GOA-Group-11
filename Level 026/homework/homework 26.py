def manual_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

print(manual_sum([1, 2, 3, 4]))



def max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst[1:]:
        if num > max_value:
            max_value = num
    return max_value

print(manual_sum([1, 2, 3, 4]))


def min(lst):
    if not lst:
        return None
    min_value = lst[0]
    for num in lst[1:]:
        if num < min_value:
            min_value = num
    return min_value

print(min([1, 2, 3, 4]))


def manual_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

print(manual_len([3, 2, 3, 2, 3, 2, 3, 2]))