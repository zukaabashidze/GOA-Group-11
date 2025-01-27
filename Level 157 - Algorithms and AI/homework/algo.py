def pr(lst):
    print(" ".join(map(str, lst)))

def main():
    lst = [6, 4, 2, 1, 18, 17, 12]
    N = len(lst)

    pr(lst)

    for i in range(1, N):
        new_element = lst[i]
        location = i - 1

        while location >= 0 and lst[location] > new_element:
            lst[location + 1] = lst[location]
            location -= 1

        lst[location + 1] = new_element

    pr(lst)

if __name__ == "__main__":
    main()
