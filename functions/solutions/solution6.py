def to_listing(first_name, last_name, num):
    """ (str, str, str) -> str
    The first parameter is a first name, the second is a last name, and the third parameter is a phone number.     Return a string in the format "LAST_NAME, FIRST_NAME: PHONE_NUMBER", where LAST_NAME, FIRST_NAME, and     PHONE_NUMBER are replaced by the given last name, first name and phone number.

    >>> to_listing('David', 'Cohen', '12345')
    'Cohen, David: 12345'
    """
    return last_name + ', ' + first_name + ': ' + num
