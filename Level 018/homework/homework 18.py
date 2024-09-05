def filtered_arr(start_num, end_num):
    numbers = []
    filtered_list = []

    for i in range(start_num, end_num):
        numbers.append(i)

    print(numbers)

    for i in numbers:
        if i % 2 == 0:
            filtered_list,append(i ** 2)
        else:
            filtered_list.append(i * 0.5)
    return filtered_list



start_num = int(input("please enter your start number : "))
end_num  = int(input("please enter end number:" ))



def even_index(lastname):
    even_index_list = []
    for i in range(len(lastname)):
        if i % 2 == 0:
            even_index_list.append(lastname[i])
            print(lastname[i])
            