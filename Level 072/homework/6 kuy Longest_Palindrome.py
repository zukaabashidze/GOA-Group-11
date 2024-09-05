def longest_palindrome (s):
    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                max_len = max(max_len, len(substring))
    return max_len