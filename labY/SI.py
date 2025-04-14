class SI:
    prefixes = ['Q', 'R', 'Y', 'Z', 'E', 'P', 'T', 'G', 'M', 'k', 'h', 'da',
                'd', 'c', 'm', 'μ', 'n', 'p', 'f', 'a', 'z', 'y', 'r', 'q'] 
    exponents = [30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 2, 1, -1, -2, -3, -6,
                 -9, -12, -15, -18, -21, -24, -27, -30]

def SI_index(title):
    title = title.split(',')
    if len(title) < 2:
        err = (f"{title} is unreadable title format.\n"
        + "correct format: \"{Quantity}, {prefix}{symbol}\"\n"
        + "example: \"I, μA\"\n")
        raise ValueError(err)

    quantity = title[0].strip()
    symbol   = title[1].strip()

    for i in range(len(SI.prefixes)):
        p = SI.prefixes[i]
        if symbol[0:1] == 'da':
            return i
        if symbol[0] == p:
            return i
    raise ValueError("unable to parse columns units")

def units(title):
    i = SI_index(title)
    return SI.prefixes[i]

def exponent(title):
    i = SI_index(title)
    return SI.exponents[i]
