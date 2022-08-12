def wiw_sort(word, words):
    if word == words[0] + words[1]:
        return words
    else:
        words.reverse()
        return words