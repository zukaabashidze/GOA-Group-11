def longest_length():
    end = "ctrlc"
    longest = ""
    text = input()
    while text != end:   
        if len(longest) < len(text):
            longest = text
        text = input()
    return f"Longest text: {text} n/ Length: {len(text)}"


