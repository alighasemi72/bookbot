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


def sort_on(item):
    return item["num"]


def sorted_charachters_count(chars_dict):
    chars_list = []
    for chd in chars_dict:
        chars_list.append({"name": chd, "num": chars_dict[chd]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
