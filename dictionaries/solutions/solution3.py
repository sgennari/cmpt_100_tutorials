def is_one_to_one(d):
    """
    (dict of {str: int}) -> bool

    Return True if and only if no two of d's keys
    map to the same value.

    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
    True
    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
    False
    >>> is_one_to_one({})
    True
    """
    values = []
    for val in d.values():
        if val in values:
            return False
        values.append(val)
    return True
