def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ''
    for char in phrase:
        if char == to_swap.lower() or char == to_swap.upper():
            if char.isupper():
                new_char = char.lower()
            else:
                new_char = char.upper()
        else:
            new_char = char
        new_phrase += new_char
    return new_phrase
