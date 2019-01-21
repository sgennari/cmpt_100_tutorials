def earlier_name(name1, name2):
    """ (str, str) -> str
    Return the name, name1 or name2, that comes first alphabetically.
    >>> earlier_name('Jen', 'Paul')
    'Jen'
    >>> earlier_name('Colin', 'Colin')
    'Colin'
    """
    if name1 < name2:
      return name1
    else:
      return name2
  