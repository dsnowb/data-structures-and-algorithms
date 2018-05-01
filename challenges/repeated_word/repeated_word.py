def repeated_word(string):
    """Return the first word repeated in string argument, space separated."""
    if type(string) is not str:
        raise TypeError('argument must be of type <str>.')

    words = set()
    punct = {'"', ',', '.', ':', ';', ' ', '!', '?', '-', '—'}
    word = ''
    for ch in string:
        if ch in punct:
            print(word)
            if word.lower() in words:
                return word.lower()
            if len(word):
                words.add(word.lower())
            word = ''

        else:
            word += ch
