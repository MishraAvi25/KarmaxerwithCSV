from Title_Parser import get_titles

title = get_titles()

def word_count(string):
    tokens = string.split()
    n_tokens = len(tokens)
    return n_tokens

def all_titles():
    title_length = []
    for items in title:
        length = word_count(items)
        title_length.append(length)
    return title_length