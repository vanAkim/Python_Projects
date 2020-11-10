def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(30)
    1
    >>> num_buses(50)
    1
    >>> num_buses(0)
    0
    """
    import math
    return math.ceil(n/50)


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([-1, -0.2, -4])
    (0, -5.2)
    >>> stock_price_summary([1, 0.2, 4])
    (5.2, 0)
    """

    losses = 0
    gains = 0
    for item in price_changes:
        if item > 0:
            gains = gains + item
        else:
            losses = losses + item

    return (gains, losses)

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 0)
    >>> nums
    [1, 2, 3, 4, 5, 6]
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 3)
    >>> nums
    [4, 5, 6, 1, 2, 3]
    >>> nums = [1]
    >>> swap_k(nums, 0)
    >>> nums
    [1]
    """

    for i in range(k):
        tempo = L[i]
        L[i] = L[-k + i]
        L[-k + i] = tempo


if __name__ == '__main__':
    import doctest
    doctest.testmod()
