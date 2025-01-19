# Hashtag Generation
def generate_hashtag(s):
    s1 = s.split()
    list = []
    for i in s1:
        list.append(i.title())
    if len(s) >= 140 or s == '':
        return False

    else:
        return "#" + "".join(list)