def format_name(first, last):
    """ (str, str) -> str

    Return the given first and last name as a single string, in the form: LAST_NAME, FIRST_NAME where LAST_NAME and FIRST_NAME are replaced by last and first. Mononymous persons (those with no last name) should have their name
    returned without a comma.

    >>> format_name('Cherilyn', 'Sarkisian')
    'Sarkisian, Cherilyn'
    >>> format_name('Cher', '')
    'Cher'
    """
    if last == '':
	    return first
    else:
	    return last + ',' + first