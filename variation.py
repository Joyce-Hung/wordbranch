def find_variation(voc, char):
    a = 0
    charlist = []
    for x in char:
        if x in voc:
            charlist.append(x)

    if len(charlist) == 0:
        return char[0]
    else:
        for i in charlist:
            if (a < len(i)):
                a = len(i)
        return i
