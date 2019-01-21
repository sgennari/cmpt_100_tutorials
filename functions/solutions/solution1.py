def total_slices(num_pizzas, slices_per_pizza):
    """ (int, int) -> int

    Return the total number of slices in num_pizzas pizzas that each have slices_per_pizza slices.

    >>> total_slices(2, 30)
    60
    >>> total_slices(1, 8)
    8
    """
    return num_pizzas*slices_per_pizza