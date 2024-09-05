def friend(x):
    friend_names = []
    
    for name in x:
        if len(name) == 4:
            friend_names.append(name)
    return friend_names