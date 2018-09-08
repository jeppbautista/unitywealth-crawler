def get_captcha(file):
    d = {}
    with open(file) as read:
        for i, line in enumerate(read):
            d[i+1] = line.strip()

    return d
