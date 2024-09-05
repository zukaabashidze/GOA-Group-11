# word = "zukaabashidze"

# print(word.replace("a","d"))


# def my_replace(word, replace_char, input_char):
#     change_word = ""  # initialize an empty string to store the result
#     for char in word:
#         if char == replace_char:
#             change_word = change_word + input_char
#         else:
#             change_word = change_word + char
#     return change_word   

# print(my_replace("zukaabasshidze", "s " , "b"))        

def evens(numbers_list):
    count = 0
    for number in numbers_list:
        if number % 2 == 0:
            count = count +1 
    return count

print(evens([2,1,4,7,5]))




