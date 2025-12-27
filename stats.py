def words_counter(string):
    words = string.split()
    return len(words)


def charachters_count(string):
    chars = {}
    for ch in list(string):
        key = ch.lower()
        if key in chars:
            chars[key] += 1
        else:
            chars[key] = 1
    return chars
