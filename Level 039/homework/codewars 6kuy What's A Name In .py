def name_in_str(strng : str, name : str) -> bool:
    strng = strng.lower()
    name = name.lower()
    
    name_ku = 0 

    for char in strng:
          if char == name[name_ku]:

            name_ku += 1

            if name_ku == len(name):

                return True

    
    return False