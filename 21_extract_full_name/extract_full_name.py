names = [{'first': 'Ada', 'last': 'Lovelace'},{'first': 'Grace', 'last': 'Hopper'},]

def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    names_list = []
    for person in people:
        full_name = ''
        for name in person.values():
            full_name += name + ' '
        names_list.append(full_name.strip())
    return names_list

