def same_abs(num1, num2):
    """ (number, number) -> bool
    Return True iff (if and only if)
    num1 and num2 have the same absolute value.
    >>> same_abs(-3, 3)
    True
    >>> same_abs(3, 3.5)
    False
    """
    return abs(num1) == abs(num2)