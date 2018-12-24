def build_placements(shoes):
    """ (list of str) -> dict of {str: list of int}
    Return a dictionary where each key is a company
    and each value is a
    list of placements by people wearing shoes
    made by that company.

    >>> result = build_placements(['Saucony', 'Asics', \
            'Asics', 'NB', 'Saucony', 'Nike', 'Asics', 'Adidas', \
            'Saucony', 'Asics'])

    >>> result == {'Saucony': [1, 5, 9], \
    'Asics': [2, 3, 7, 10], 'NB': [4], 'Nike': [6], \
    'Adidas': [8]}
    True
    """
    placements = {}
    position = 1
    for brand in shoes:
        if brand not in placements:
            placements[brand] = []
        placements[brand].append(position)
        position = position + 1
    return placements
