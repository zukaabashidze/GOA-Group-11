def remove_url_anchor(url):
    if "#" in url:
        index = url.index("#")
        return url[:index]
    else:
        return url