import random


def breed(p1, p2, low, high):
    """
    Takes two parents and creates a child using crossing-over
    :param p1: Parent 1, a one-hot representation
    :param p2: Parent 2, a one-hot representation
    :param low: The minimum fraction of parent one to be used
    :param high: The maximum fraction of parent one to be used
    :return: A one-hot representation of a child after crossing-over
    """
    lower_bound, upper_bound = int(len(p1) * low), int(len(p1) * high)
    index = random.randint(lower_bound, upper_bound)

    child = p1[0:index] + p2[index:len(p1)]

    return child