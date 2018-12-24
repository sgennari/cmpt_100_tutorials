def invert_dictionary(d):
    """ (dict) -> dict

    Precondition: Values of d are immutable

    Return a new dictionary where the keys in the new dictionary are
    the values from d, and the values are lists of the keys
    that are associated with those values from d.

    >>> invert_dictionary({"cherry": "red", "pomegranate": "red"})
    {'red': ['cherry', 'pomegranate']}
    """
    inverted = {}
    for key, val in d.items():
        if val not in inverted:
            inverted[val] = []
        inverted[val].append(key)

    return inverted
