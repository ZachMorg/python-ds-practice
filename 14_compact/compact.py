def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    falsy = [0, 0.0, '', None, False, [], {}, ()]
    truthy_list = []
    for item in lst:
        if item not in falsy:
            truthy_list.append(item)
    return truthy_list