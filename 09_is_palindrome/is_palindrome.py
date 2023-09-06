def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    reg_phrase = phrase.replace(' ','')
    reg_phrase = reg_phrase.lower()
    back_phrase = list(reg_phrase)
    back_phrase.reverse()
    back_phrase = ''.join(back_phrase)
    return reg_phrase == back_phrase
