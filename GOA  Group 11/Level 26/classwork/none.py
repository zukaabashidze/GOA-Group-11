# Friden or Foe
def friend(x):
    friend_names = []
    
    for name in x:
        if len(name) == 4:
            friend_names.append(name)
    return friend_names

# Get the Middle Character
def get_middle(s):
    lenght = len(s)
    
    middle = lenght // 2
    
    if lenght % 2 == 1:
        return s[middle]
    else:
        return s[middle - 1: middle + 1]
    
#Highest and Lowest 
# ეტა ოჩენ გაუგებელ 
# 


# Sum of two Lowest positive integer
# ესეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეეც