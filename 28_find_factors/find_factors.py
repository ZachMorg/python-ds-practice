def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    result = []
    num_list = list(range(num+1))
    num_list.pop(0)
    for val in num_list:
        if num % val == 0:
            result.append(val)
    return result