def duplicate_encode(word):
    word = word.lower()
    
    result = ''.join(['(' if word.count(char) == 1 else ')' for char in word])
    
    return result