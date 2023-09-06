def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_phrase = []
    phrs = phrase.lower().split(' ')
    for word in phrs:
        new_phrase.append(word.capitalize())
    return ' '.join(new_phrase)