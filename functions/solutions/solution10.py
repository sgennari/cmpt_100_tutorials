def can_vote(age):
    """ (int) -> bool
    Return True iff age is legal voting age of at least 18 years.
    >>> can_vote(16)
    False
    >>> can_vote(21)
    True
    """
    return age >= 18
