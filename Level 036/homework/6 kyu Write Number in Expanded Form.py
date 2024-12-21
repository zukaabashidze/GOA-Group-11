

def expanded_form(num):
    num_string = str(num)
    result = []
    for i in range(len(num_string)):
        if num_string[i] != '0':
            result.append(num_string[i] + '0' * (len(num_string) - i - 1))
    return " + ".join(result)