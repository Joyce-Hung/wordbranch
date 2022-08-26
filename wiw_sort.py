def wiw_sort(word, words):

    m = 0
    n = 0
    length = 0
    count = 0

    if (len(words[0]) > len(words[1])):
        words.reverse()
    for y in words[0]:
        length += 1
        if (length <= len(words[0])):
            for x in word:
                if x == y:
                    m = m + word.index(x)
    for j in words[1]:
        count += 1
        if (count <= len(words[0])):
            for i in word:
                if i == j:
                    n = n + word.index(i)
    cal(m, n, words)
    return words


def cal(m, n, words):
    if m > n:
        words.reverse()
        return words
