def get_middle(s):
    lenght = len(s)
    
    middle = lenght // 2
    
    if lenght % 2 == 1:
        return s[middle]
    else:
        return s[middle - 1: middle + 1]